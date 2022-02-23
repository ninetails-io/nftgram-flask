from datetime import datetime
from flask_restful import Resource, reqparse
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.db import get_db
import re
import json
from src.const import ENV

# parser used by both User class and Users class
parser = reqparse.RequestParser()

class User(Resource):
    def get(self, user_name):
        query = 'SELECT * FROM users WHERE username="?"'
        result = get_db().cursor().execute(query, user_name)
        row = result.fetchone()
        return dict(zip([c[0] for c in result.description], row))

    def post(self):

        try:
            # set the arguments to be parsed out of the request (JSON)
            parser.add_argument('username')
            parser.add_argument('password')
            data = parser.parse_args()
            print(data)

            # check the username
            un = data['username']

            # match returns null if the pattern is not matched
            match = re.match('^[A-Za-z]+[A-Za-z0-9_]{2,15}$', un)
            if not match:
                raise Exception("Username must begin with a letter and contain only letters, numbers, and underscore")

            # user id is a integer hash of the username
            uid = hash(data[un])

            # password must contain at least 4 characters
            if len(data['password']) < 4:
                raise Exception("Password must contain at least 4 characters")

            # get the secure password hash
            pw = generate_password_hash(data['password'])
            dt = datetime.utcnow()

            # attempt to insert the record into the database
            values = (uid, un, pw, dt)
            query = "INSERT INTO users(id, username, password, date_joined) VALUES (?,?,?,?)"
            try:
                get_db().cursor().execute(query, values)
                get_db().commit()
                get_db().close()
            except:
                raise Exception("Could not add user to database")

            return parser.parse_args(), 200
        except Exception as e:
            message = getattr(e, 'message', repr(e))
            # if dev or development return error message in JSON
            if (ENV[0.3].lower()) == "dev":
               return json.dumps({"error":getattr(e, 'message', repr(e))}), 401
            else:
                return json.dumps({"error":"Unable to add user"}), 401


class Users(Resource):
    def get(self):
        result = get_db().cursor().execute('SELECT * FROM users')
        rows = result.fetchall()
        get_db().close()
        response = []
        for row in rows:
            response.append(dict(zip([c[0] for c in result.description], row)))
        return response
