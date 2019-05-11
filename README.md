Flask application template
==========================

Template for simple Flask application, including a blueprint for basic user profiles and password reset by email.  With basic Bootstrap 4 styling.

##Blueprints
- User authorisation is handled by the `auth` blueprint
- Main application logic is handled by the `main` blueprint

##Database
Database tables are represented by models defined in `models.py`

To add new tables to the database:
- Add new models in `models.py`
- Create a migration script to update the database with `flask db migrate -m "message"`
- Upgrade the database with `flask db upgrade`