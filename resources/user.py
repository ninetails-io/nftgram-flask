from flask_restful import Resource
from flask import jsonify
from src.db import get_db

class User(Resource):
    def get(self, user_name):
        return get_db().cursor().execute(f'SELECT * FROM users WHERE user_name={user_name}').fetchone()
class Users(Resource):
    def get(self):
        result = get_db().cursor().execute('SELECT * FROM users').fetchall()
        return jsonify(result)