from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
import os

from app.commands import create_user, delete_user

logging.basicConfig(level=logging.DEBUG, filename='log')

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'
login.login_message_category = 'danger'

# register backend admin commands
app.cli.add_command(create_user)
app.cli.add_command(delete_user)

app.secret_key = os.environ['FLASK_SECRET_KEY']

from app import views, models