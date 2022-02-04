from flask_restful import Resource

users = {
    87: {'username': 'user1', 'password': 'password1'},
    92: {'username': 'user3', 'password': 'abcd' }
}
class User(Resource):
    def get(self, user_id):
        if user_id and user_id in users:
            return users[user_id]
        return 404
class Users(Resource):
    def get(self):
        return users