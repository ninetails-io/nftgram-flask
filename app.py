# Sean_Jones
# Jason
# Adam Kohler
# Stephen Gomez-Fox

import os
from flask import Flask
from flask_restful import Resource, Api
from os.path import exists
import sqlite3
from src.migrate_db import init_db
from src.const import DB_FULLPATH
from flask import g
from resources.user_resource import UserResource, UsersResource
from resources.auth_resource import Signup, Login
from resources.blank_resource import BlankResource, BlanksResource
from resources.test_resource import Test
from src.tools import error_response

app = Flask(__name__)
app.config.from_object('src.config.DevelopmentConfig')
api = Api(app)

# in debug, the app runs twice automatically.
# in this case, delete the database the first time
if app.debug and os.environ.get("WERKZEUG_RUN_MAIN") == "false" and exists(DB_FULLPATH):
    os.remove(DB_FULLPATH)

# create and populate the database if the db file doesn't exist
if not exists(DB_FULLPATH):
    init_db()


# TODO: Determine if a root response is required

# Associate resource paths with resource classes
api.add_resource(UserResource, '/user', '/user/<string:username>')
api.add_resource(SignupResource, '/signup')
api.add_resource(LoginResource, '/login')
api.add_resource(BlankResource, '/blank', '/blank/<int:id>')
api.add_resource(BlanksResource, '/blanks')
api.add_resource(Test,  '/')


# @app.errorhandler(Exception)
# def basic_error(e):
#     return error_response("UNKNOWN_ERROR", "An unknown error has occurred"), 500


# neatly exit in case of exception
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Run app.py if the current module being run is main.py
if __name__ == '__main__':
    app.run(debug=True)
