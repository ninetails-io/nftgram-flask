from datetime import datetime
from flask_restful import Resource, reqparse
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.db import get_db

parser = reqparse.RequestParser()


class User(Resource):
    def get(self, user_name):
        result = get_db().cursor().execute(f'SELECT * FROM users WHERE username="{user_name}"')
        row = result.fetchone()
        return dict(zip([c[0] for c in result.description], row))

    def post(self):

        parser.add_argument('username')
        parser.add_argument('password')
        data = parser.parse_args()
        id = hash(data[username])
        un = data['username']
        pw = data['password']
        dt = datetime.utcnow()
        hashed_pw = generate_password_hash(pw)
        values = (id, un, pw, dt)
        query = "INSERT INTO users(id, username, password, date_joined) VALUES (?,?,?,?)"
        get_db().cursor().execute(query, values)
        get_db().commit()
        get_db().close()
        return parser.parse_args()


class Users(Resource):
    def get(self):
        result = get_db().cursor().execute('SELECT * FROM users')
        rows = result.fetchall()
        get_db().close()
        response = []
        for row in rows:
            response.append(dict(zip([c[0] for c in result.description], row)))
        return response
