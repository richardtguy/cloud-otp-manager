"""
Database model definitions
"""
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time
import jwt
import logging
from app import db, login

logger = logging.getLogger(__name__)

"""
User database models
"""
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
	"""
	Database model for user accounts
	"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def get_reset_password_token(self, expires_in=600):
		return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in},
											current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

	@staticmethod
	def verify_reset_password_token(token):
		try:
			id = jwt.decode(token, current_app.config['SECRET_KEY'],
											algorithms=['HS256'])['reset_password']
		except:
			return
		return User.query.get(id)

	def __repr__(self):
		return '<User {}>'.format(self.username)

"""
Database models
"""
class Account(db.Model):
    """
    Database model for an OTP account
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    key = db.Column(db.String(64))
    # backref sets up a reference from the right side of this relationship
    # (the User).  Accessing User.accounts returns a (lazy-loaded) list of
    # accounts associated with the user.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('accounts', lazy=True, order_by='Account.name'))

    def __repr__(self):
        return '<Account {}>'.format(self.name)
