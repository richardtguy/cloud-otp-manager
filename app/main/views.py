"""
Main application view functions
"""
from flask import render_template
from flask_login import current_user, login_required

from app import db
from app.main import bp

import logging
logger = logging.getLogger(__name__)

@bp.route("/", methods=["GET"])
@login_required
def index():
	return render_template('index.html')
