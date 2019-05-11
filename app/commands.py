"""
Command line functions for back-end admin
"""
import click
import logging

import app

logger = logging.getLogger(__name__)

@click.command('create_user')
@click.option('--username', '-u', prompt=True)
@click.option('--password', '-p', prompt=True)
def create_user(username, password):
	"""
	Create new user
	"""
	u = app.models.User(username=username)
	u.set_password(password)
	try:
		app.db.session.add(u)
		app.db.session.commit()
		click.echo("Created user: {}".format(u))
	except:
		app.db.session.rollback()
		click.echo("Error! Could not create user")
	finally:
		app.db.session.close()
	
@click.command('delete_user')
@click.option('--username', '-u', prompt=True)
def delete_user(username):
	"""
	Delete user
	"""
	u = app.models.User.query.filter_by(username=username).first()
	try:
		app.db.session.delete(u)
		app.db.session.commit()
		click.echo("Deleted user: {}".format(username))
	except:
		app.db.session.rollback()
		click.echo("Error! Could not delete user")
	finally:
		app.db.session.close()