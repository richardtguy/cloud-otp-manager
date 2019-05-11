Flask application template
==========================

Template for simple Flask application, including a blueprint for basic user profiles and password reset by email.  With basic Bootstrap 4 styling.

## Blueprints
- User authorisation is handled by the `auth` blueprint
- Define main application logic in the `main` blueprint

## Database
The `auth` and `main` blueprints share a single database object, `db`.  Database tables are represented by models defined in `models.py`

To add new tables to the database:
- Add new models in `models.py`
- Create a migration script to update the database with `flask db migrate -m "message"`
- Upgrade the database with `flask db upgrade`

## Configuration
Ensure the following configuration variables are set (e.g. in `/instance/config.py` for local development):

- `SQLALCHEMY_DATABASE_URI`: Database URI
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Set to `False`
- `ADMINS`: "From" address for admin emails
- `SECRET_KEY`: Flask application secret key
- `MAIL_USERNAME`: Username for email server
- `MAIL_PASSWORD`: Password for email server
- `MAIL_SERVER`: Email server address
- `MAIL_PORT`: Email server port
- `MAIL_USE_SSL`: Set to `True` to use SSL
