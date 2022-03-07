from src.tools import valid_username, valid_password, encode_auth_token, decode_auth_token
from datetime import datetime
from flask import jsonify
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
import json
from src.tools import valid_username, valid_password, encode_auth_token, decode_auth_token
from src.db import get_db
import src.const
from src.tools import valid_username, valid_password, to_dict, to_dict_array

parser = reqparse.RequestParser()
token_store = dict()


class SignupResource(Resource):
    def post(self):
        try:
            # ARGUMENT PARSING

            # select the arguments to be parsed out of the request (JSON)
            parser.add_argument('username')
            parser.add_argument('password')
            data = parser.parse_args()

            # get the parsed argument values
            user_id = str(data['username'])
            password_text = str(data['password'])

            # SANITY CHECKING

            # match returns null if the pattern is not matched
            if not valid_username(user_id):
                raise Exception("Username must begin with a letter and contain only letters, numbers, and underscore")

            # password must contain at least 4 characters
            if not valid_password(password_text):
                raise Exception("Password does not meet requirements")

            # PREPARE TO INSERT INTO DATABASE

            # get the secure password hash
            password_hash = generate_password_hash(password_text)
            print("Added user "+user_id+" pw="+password_text)
            dt = datetime.utcnow()

            # attempt to insert the new user into the database
            values = (user_id, password_hash, dt)
            query = "INSERT INTO users(user_id, password, date_joined) VALUES (?,?,?)"

            # PERFORM THE INSERT
            try:
                get_db().cursor().execute(query, values)
                get_db().commit()
                get_db().close()
            except Exception as e:
                print(e)
                raise Exception("Could not add user to database")

            # CREATE AND RETURN NEW JWT TOKEN
            token = encode_auth_token(user_id)
            print(json.dumps(token, indent=4))
            # store the new token in the token store and return it
            token_store[user_id] = token
            return jsonify({"token": token.decode('utf-8')})

        # ERROR HANDLING
        except Exception as e:
            get_db().close()
            return 401


class LoginResource(Resource):
    def post(self):
        # log in to an existing account and generate a new auth token for user
        parser.add_argument('username')
        parser.add_argument('password')
        data = parser.parse_args()

        # get record from the database
        query = 'SELECT * FROM users WHERE user_id=?'
        result = get_db().cursor().execute(query, (data['username'],))
        user = to_dict(result.description, result.fetchone())

        if check_password_hash(user['password'], data['password']):
            token = encode_auth_token(data['username'])
            token_store[data['user_id']] = token
            return jsonify({"token": token.decode('utf-8')})
        else:
            get_db().close()
            return 401
