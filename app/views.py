"""
Minimal Flask application with user login
"""
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
import os
import json
import logging

from app import app, db
from app.models import User
import config

logger = logging.getLogger(__name__)

@app.route("/", methods=["GET"])
@login_required
def index():
	return render_template('index.html')
	
@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		if current_user.is_authenticated:
			return redirect(url_for('index'))
		user = User.query.filter_by(username=request.form['username']).first()
		print(request.form['password'])
		if user is None or not user.check_password(request.form['password']):
			flash('Invalid username or password', 'danger')
			return redirect(url_for('login'))
		login_user(user)
		next_page = request.args.get('next')
		if not next_page or urlparse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	
	return render_template('login.html')
	
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
