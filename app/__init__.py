from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
import os

logging.basicConfig(level=logging.DEBUG, filename='log')

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
login.login_message_category = 'danger'

app.secret_key = os.environ['FLASK_SECRET_KEY']

from app import views, models