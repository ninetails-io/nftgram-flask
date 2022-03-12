from flask_restful import Resource, reqparse
from flask import make_response, Request, request
from werkzeug.security import generate_password_hash, check_password_hash
from src.db import get_db
from entities.user_entity import User
from src.tools import to_dict, to_dict_array, error_response, valid_username, valid_password
from src.token_store import jwt_user_from_request, jwt_token_from_request

# parser used by both User class and Users class
from token_store import jwt_current_token

parser = reqparse.RequestParser()


# TODO: Move CRUD operations to functions

class UserResource(Resource):
    def get(self, username):
        # retrieves user from database and returns as flask response
        user = dict()

        # ensure a valid user is logged on
        try:

            token = jwt_token_from_request(request)
            if token is None:
                return error_response("UNAUTHORIZED", "Missing or invalid authentication token. Please login again.", 401)
            user_id = jwt_user_from_request(request)
            if user_id is None:
                return error_response("UNAUTHORIZED", "Invalid or expired token. Please login again.", 401)
        except Exception as e:
            return error_response("UNKNOWN_ERROR", "Token Validation caused a failure")


        try:
            query = 'SELECT * FROM users WHERE user_id=?'
            values = (username,)
            result = get_db().cursor().execute(query, values)
            row = result.fetchone()
            user = to_dict(result.description, row)
            password = "********"
            # determine the password to be returned based on authorization

            # if admin, replace password with hashed value from db
            # if authorized password=row["password"]
            # TODO: authorization

            # NOTE: dictionary results always alphanumeric. OrderedDict
            #       does not solve problem; once jsonified order is lost
            # TODO: look into flask templates for alternative way to control order of fields
            result_dict = {"user_id": user["user_id"], "password": password, "date_joined": user["date_joined"]}
            resp = make_response(result_dict, 200)
            resp.headers['Authorization'] = token;
            return resp

        except Exception as e:
            print(e)
            return error_response()

    def put(self, username):
        # performs an update of an existing user (only password can be changed)

        try:
            # verify the token, and ensure it belongs
            # to the user being updated
            token = jwt_token_from_request(request)
            if token is None:
                return error_response("UNAUTHORIZED", "Missing or invalid authentication token. Please login again.", 401)
            token_user = jwt_user_from_request(request)
            if token_user is None:
                return error_response("UNAUTHORIZED", "Invalid or expired token. Please login again.", 401)

            # set the arguments to be parsed out of the request (JSON)
            parser.add_argument('password')
            data = parser.parse_args()

            # get the new password from the parser
            pw = str(data['password'])

            if not (username == token_user or token_user == "admin"):
                return error_response("UNAUTHORIZED", "Can only change logged in user")

            # check that updated password is a valid format
            if not valid_password(pw):
                raise Exception("Password does not meet requirements")

            # get the user record from the database
            try:
                values = (username,)
                query = 'SELECT * FROM users WHERE user_id=?'
                result = get_db().cursor().execute(query, values)
                user = to_dict(result.description, result.fetchone())

            except Exception as e:
                # return an error if user not found
                return error_response("NOT_FOUND", "User not found", 404)

            try:
                # get the secure password hash
                pw_hash = generate_password_hash(pw)

                # retain the existing date_joined, regardless of request
                dt = user["date_joined"]

                # attempt to update the user into the database
                values = (username, pw_hash, dt, username)
                query = 'UPDATE users SET user_id=?, password=?, date_joined=? WHERE user_id=?;'
                get_db().cursor().execute(query, values)
                get_db().commit()
                get_db().close()

                # return the updated user, with the password hidden
                payload = {"user_id": username, "password": "********", "date_joined": dt}

                # put and post return 201 on success
                resp = make_response(payload, 201)
                resp.headers["Authorization"] = "Bearer " + token
                return resp

            except Exception as e:
                print(repr(e))
                return error_response("UNKNOWN", "An unknown error has occurred", e)
        except Exception as e:
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
