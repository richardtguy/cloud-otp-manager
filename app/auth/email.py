"""
Email functions
"""
from flask_mail import Message
from flask import render_template, current_app
from app import mail

import logging
logger = logging.getLogger(__name__)

def send_password_reset_email(user):
	"""
	Send password reset email to user
	"""
	token = user.get_reset_password_token()
	send_email(
		'Reset Your Password',
		sender=current_app.config['ADMINS'][0],
		recipients=[user.username],
		text_body=render_template('email/reset_password.txt',
															user=user, token=token),
		html_body=render_template('email/reset_password.html',
															user=user, token=token)
	)

def send_email(subject, sender, recipients, text_body, html_body):
	"""
	Send email
	"""
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)