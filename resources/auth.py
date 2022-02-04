from flask_restful import Resource

class Signup(Resource):
    def post(self, credentials):
        return 'signing up'