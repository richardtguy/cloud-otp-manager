import os

# Flask application configuration
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'itsasecret'

# Arbitrary salt for strong encryption
SALT = os.environ.get('OTP_SALT') or \
	b'\xe9K\x0b\x9dx\r\xe0\xdd:\x91\xfa\x8dP\xbat\x97'

# Email address for admin
ADMINS = [os.environ.get('ADMIN')]

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Email server configuration
MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
MAIL_SERVER=os.environ.get('MAIL_SERVER')
MAIL_PORT=os.environ.get('MAIL_PORT')
MAIL_USE_SSL=os.environ.get('MAIL_USE_SSL')

# Log to stdout if deployed to Heroku
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
