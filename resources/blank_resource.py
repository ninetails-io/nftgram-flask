from datetime import datetime
import json
import uuid
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from src.tools import to_dict, to_dict_array, decode_auth_token, error_response
from src.db import get_db
from src.const import ENV

# import a token store after implementation

parser = reqparse.RequestParser()


class BlankResource(Resource):

    def get(self, id=None):
        # Blank resource that takes and ID and returns an empty object

        if id is None:
            return error_response("BAD_REQUEST", "Missing id", 400)

        try:
            # validate token
            # parameterize query and execute returning result, and close connection
            # put resulting payload into dict, jsonify and return
            payload = to_dict()
            return make_response(payload, 200)
        except:  # must be the last except clause
            return error_response("UNKNOWN_ERROR", "An unknown error has occurred", 500)

    def post(self):

        try:
            # add arguments from the post request and parse
            # put the arguments into variables for convenience
            # create an integer id using an appropriate method eg: id = int(uuid.uuid4())
            # parameterize query and insert using a tuple (add extra comma to tuple if only one parameter)
            # close the connection
            # build payload dict from generated id and provided arguments, jsonify, and return
            payload = to_dict()
            return make_response(payload, 201)
        # this must be the last except clause
        except:
            return error_response("UNKNOWN_ERROR", "An unknown error has occurred", 500)

        # similar approach for PUT and DELETE, optionally PATCH


class BlanksResource(Resource):
    def get(self):
        # Blank Resource array requires no parameters

        try:
            # validate token
            # set query string, execute returning result, and close connection
            # put resulting payload into array of dicts , jsonify and return
            payload = to_dict_array()

            # make_response does not work on arrays
            return jsonify(payload)
        # this must be the last except clause
        except:
            return error_response("UNKNOWN_ERROR", "An unknown error has occurred", 500)

        # no other verbs for get all type resource
