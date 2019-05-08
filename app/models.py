"""
Minimal database model for Flask application
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import logging
from app import db, login

logger = logging.getLogger(__name__)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# define database table for users
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
															
	def __repr__(self):
		return '<User {}>'.format(self.email)