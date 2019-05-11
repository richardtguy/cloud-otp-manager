"""
Command line functions for back-end administration of users
"""
import click
from flask.cli import with_appcontext

import logging
logger = logging.getLogger(__name__)

from app.models import User
from app import db

@click.command('create_user')
@click.option('--username', '-u', prompt=True)
@click.option('--password', '-p', prompt=True)
@with_appcontext
def create_user(username, password):
	"""
	Create new user
	"""
	u = User(username=username)
	u.set_password(password)
	try:
		db.session.add(u)
		db.session.commit()
		click.echo("Created user: {}".format(u))
	except:
		db.session.rollback()
		click.echo("Error! Could not create user")
	finally:
		db.session.close()
	
@click.command('delete_user')
@click.option('--username', '-u', prompt=True)
@with_appcontext
def delete_user(username):
	"""
	Delete user
	"""
	u = User.query.filter_by(username=username).first()
	try:
		db.session.delete(u)
		db.session.commit()
		click.echo("Deleted user: {}".format(username))
	except:
		db.session.rollback()
		click.echo("Error! Could not delete user")
	finally:
		db.session.close()