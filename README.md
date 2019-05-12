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

## Backend admin
To create a user:
`flask create_user --username user@example.com --password password`

To create a user:
`flask delete_user --username user@example.com`

## Deploy to Heroku using the Heroku CLI

Clone this repository to a folder on local computer.
`git clone https://github.com/richardtguy/flask-users-demo.git`

Add main application logic.

Create a heroku app from the folder where you cloned the application.
`heroku apps:create`

Provision a database (on the free tier).
`heroku addons:add heroku-postgresql:hobby-dev`

Check the Procfile - it should include the following commands to upgrade the database and then run the gunciorn webserver.
`web flask db upgrade; gunicorn run:app`

Set environment variables, e.g.
```
heroku config:set FLASK_APP=run.py
heroku config:set WEB_CONCURRENCY=1
heroku config:set ADMINS="Someone <example@abc.com>"
heroku config:set FLASK_SECRET_KEY=asecret
heroku config:set FLASK_ENV=production
heroku config:set MAIL_USERNAME=account@email.com
heroku config:set MAIL_PASSWORD=password
heroku config:set MAIL_SERVER=examplemail.smtp.com
heroku config:set MAIL_PORT=465
heroku config:set MAIL_USE_SSL=1
```

Commit any changes in the local repository.
`git commit -a -m "deploy to heroku"`

Deploy to the remote repository.
`git push heroku master`

## Running backend admin commands
Run backend admin commands locally, with a connection to the remote database.

Install virtual environment.
`python3 -m venv venv`

Install dependencies from `requirements.txt`.
`pip install -r requirements.txt`

Set environment variables e.g. in `.env` file.  Set the DATABASE\_URL environment variable to connect to the remote database.  Get the URI from:
`heroku config:get DATABASE_URL`

(It may also be possible to run commands directly on the dyno by starting an ssh tunnel.)
`heroku ps:exec`