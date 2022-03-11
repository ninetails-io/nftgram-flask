from datetime import datetime
from flask import request, make_response, Response
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from entities.user_entity import User
from src.tools import to_dict, to_dict_array, error_response
from src.token_store import jwt_current_token, jwt_user_from_request, jwt_token_from_request

# import a token store after implementation

parser = reqparse.RequestParser()


class Test(Resource):

    def get(self):
        # Test resource that returns the currently logged in user and their token
        token = jwt_token_from_request(request)
        if token is None: return error_response("UNAUTHORIZED", "Missing or invalid authentication token. Please login again.", 401)

        user_id = jwt_user_from_request(request)
        if user_id is None: return error_response("UNAUTHORIZED", "Invalid or expired token. Please login again.", 401)

        try:
            payload = {"jwt_user_id": user_id,
                       "jwt_token": token,
                       }

            resp = make_response(payload, 200)
            resp.headers['Authorization'] = "Bearer " + token
            return resp

        except:  # must be the last except clause
            return error_response("UNKNOWN_ERROR", "An unknown error has occurred", 500)

