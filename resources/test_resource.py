from datetime import datetime
from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse
from src.token_store import get_user_from_header, get_token_from_header, jwt_current_token
from datetime import datetime
from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
import json
from src.tools import valid_username, valid_password, error_response
from src.token_store import encode_auth_token, decode_auth_token
from src.db import get_db
import src.const
from src.tools import valid_username, valid_password, to_dict, to_dict_array

parser = reqparse.RequestParser()
# import a token store after implementation

parser = reqparse.RequestParser()


class TestResource(Resource):

    # get root resource: returns currently logged-in user
    def get(self):
        auth_header = request.headers.get("Authorization")
        tk = auth_header[7:]

        print(tk)

        user_id = get_user_from_header(tk)
        new_tk = jwt_current_token(user_id)

        resp = make_response({"user_id": user_id, "token": new_tk.decode("utf-8")}, 200)
        resp.headers.set("Authorization", "Bearer " + new_tk.decode("utf-8"))
        return resp
