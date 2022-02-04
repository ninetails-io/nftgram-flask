from flask import Flask
from flask_restful import Resource, Api
from resources.user import User, Users

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True)
