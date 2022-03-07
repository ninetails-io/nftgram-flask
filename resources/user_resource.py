from datetime import datetime
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from src.db import get_db
import re
import json
from src.const import ENV
from src.tools import to_dict, to_dict_array, error_response, db_response, db_response_array, valid_username, valid_password
from collections import OrderedDict

# parser used by both User class and Users class
parser = reqparse.RequestParser()

# TODO: Move CRUD operations to functions

class UserResource(Resource):
    def get(self, username):

        # retrieves user from database and returns as flask response
        # TODO: Require valid auth token to view user data
        try:
            query = 'SELECT * FROM users WHERE username=?'
            values = (username,)
            result = get_db().cursor().execute(query, (username,))
            row = result.fetchone()

            user = to_dict(result.description, row)

            # determine the password to be returned based on authorization
            password = "********"
            # if admin, replace password with hashed value from db
            # if authorized password=row["password"]
            # TODO: authorization

            # NOTE: dictionary results always alphanumeric. OrderedDict
            #       does not solve problem; once jsonified order is lost
            # TODO: look into flask templates for alternative way to control order of fields
            result_dict = OrderedDict([("id", user["id"]), ("username", user['username']), ("password", password), ("date_joined", user["date_joined"])])
            return make_response(result_dict, 200)

        except Exception as e:
            print(e)
            return error_response()


    def post(self):
        # performs an update of an existing user

        try:
            # verify the token, and ensure it belongs
            # to the user being updated
            # TODO: implement token store

            # set the arguments to be parsed out of the request (JSON)
            parser.add_argument('username')
            parser.add_argument('password')
            data = parser.parse_args()

            # get the username and password from the parser
            un = str(data['username'])
            pw = str(data['password'])

            # check that username and password are valid format
            if not valid_username(un):
                raise Exception("Username must begin with a letter and contain only letters, numbers, and underscore")

            if not valid_password(pw):
                raise Exception("Password does not meet requirements")

            # get the user record from the database
            try:
                values = (un,)
                query = 'SELECT * FROM users WHERE username=?'
                result = get_db().cursor().execute(query, values)
                user = to_dict(result.description, result.fetchone())

            except Exception as e:
                # return an error if user not found
                return error_response("NOT_FOUND", "User not found", 404)

            try:
                # TODO: determine if user id should be updated to new hashed username value
                uid = hash(un)

                # get the secure password hash
                pw_hash = generate_password_hash(pw)

                # retain the existing date_joined, regardless of request
                dt = user["date_joined"]

                # attempt to update the user into the database
                values = (uid, un, pw_hash, dt, un)
                query = 'UPDATE users SET id=?, username=?, password=?, date_joined=? WHERE username=?;'
                get_db().cursor().execute(query, values)
                get_db().commit()
                get_db().close()

                # return the updated user, with the password hidden
                payload = {"id": uid, "username": un, "password": "********", "date_joined": dt}

                # put and post return 201 on success
                return make_response(payload, 201)

            except Exception as e:
                return error_response("","Could not update the user record")
        except:
            # unknown error
            return error_response()




class UsersResource(Resource):
    def get(self):

        # TODO: Require valid auth token to retrieve users list
        try:
            result = get_db().cursor().execute('SELECT * FROM users')
            get_db().close()
            response_array = to_dict_array(result.description, result.fetchall())
            return make_response()
        except Exception as e:
            # return an empty dict on error
            return dict(), 400
