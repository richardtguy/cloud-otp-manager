import os

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')

ADMINS = [os.environ.get('ADMIN')]

MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
MAIL_SERVER=os.environ.get('MAIL_SERVER')
MAIL_PORT=os.environ.get('MAIL_PORT')
MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
MAIL_USE_SSL=os.environ.get('MAIL_USE_SSL')