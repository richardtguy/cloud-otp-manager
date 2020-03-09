"""
Main application view functions
"""
from flask import render_template, session, request, redirect, url_for, flash
from flask import abort
from flask_login import current_user, login_required, logout_user
from flask_table import Table, Col, LinkCol, create_table
from base64 import urlsafe_b64encode, b32decode
from time import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA1, SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.fernet import Fernet, InvalidToken

from app import db
from app.main import bp
from app.models import Account, User

import logging
logger = logging.getLogger(__name__)

class BaseTable(Table):
	classes = ['table']
	thead_classes = ['thead-light']

	def get_tr_attrs(self, item):
		try:
			item['important']
			return {'class': 'table-info'}
		except KeyError:
			return {}

def get_master_key():
	"""
	Retrieve key from session, if available, else force fresh login
	"""
	try:
		return session['master_key']
	except KeyError:
		logout_user()
		return None

def get_otp(key):
	"""
	Generate One-Time Password from key
	"""
	missing_padding = len(key) % 8
	if missing_padding != 0:
		key += '=' * (8 - missing_padding)
	try:
		byte_key = b32decode(key, casefold=True)
	except:
		return None
	totp = TOTP(
		byte_key,
		6,
		SHA1(),
		30,
		backend=default_backend(),
		enforce_key_length=False
		)
	return totp.generate(time()).decode()

def decrypt_key(encrypted_key):
	"""
	Decrypt key using master key
	"""
	fernet = Fernet(get_master_key())
	return fernet.decrypt(encrypted_key).decode()

@bp.route("/", methods=["GET"])
@login_required
def index():
	# get list of accounts from database
	u = User.query.get(current_user.id)
	TableCls = create_table(base=BaseTable).add_column('account',
		Col('Account'))
	TableCls.add_column('otp', Col('One-Time Password'))
	TableCls.add_column('delete', LinkCol('Remove', 'main.remove_account', attr='remove_symbol',
		url_kwargs=dict(id='id')))
	TableCls.add_column('reveal', LinkCol(u'Show key', 'main.show_key', attr='show_symbol',
		url_kwargs=dict(id='id')))
	try:
		table = TableCls([dict(
			account=a.name,
			otp=get_otp(decrypt_key(a.key)),
			id=a.id,
			remove_symbol='\u274E',
			show_symbol='\U0001F441'
		) for a in u.accounts])
	except TypeError:
		flash('Session expired - please log in again.', 'warning')
		return redirect(url_for('auth.login'))
	return render_template('index.html', table=table)

@bp.route("/add_account", methods=["GET", "POST"])
@login_required
def add_account():
	if request.method == 'POST':
		# encrypt key using the user's master key before storing in the database
		fernet = Fernet(get_master_key())
		key_encrypted = fernet.encrypt(request.form['key'].replace(" ","")
			.encode())
		a = Account(
			name = request.form['account_name'],
			key = key_encrypted,
			user = User.query.get(current_user.id)
		)
		db.session.add(a)
		try:
			db.session.commit()
			flash("Added '{}'".format(a.name), 'success')
		except:
			db.session.rollback()
			flash("Oops! Something went wrong...", 'danger')
			raise
		finally:
			db.session.close()
		return redirect(url_for('main.index'))
	return render_template('add_account.html')

@bp.route("/remove_account/<int:id>", methods=["GET"])
@login_required
def remove_account(id):
	u = User.query.get(current_user.id)
	a = Account.query.filter_by(user=u).filter_by(id=id).first()
	if a == None:
		abort(401)
	try:
		db.session.delete(a)
		db.session.commit()
		flash('Removed account: {}'.format(a.name), 'success')
	except:
		db.session.rollback()
		click.echo("Error! Could not delete account")
	finally:
		db.session.close()
	return redirect(url_for('main.index'))

@bp.route("/show_key/<int:id>", methods=["GET"])
@login_required
def show_key(id):
	u = User.query.get(current_user.id)
	a = Account.query.filter_by(user=u).filter_by(id=id).first()
	if a == None:
		abort(401)
	key = decrypt_key(a.key)
	formatted_key = " ".join([(key[i:i+4]) for i in range(0, len(key), 4)])
	# format key for ease of reading
	flash(formatted_key, 'success')
	return redirect(url_for('main.index'))
