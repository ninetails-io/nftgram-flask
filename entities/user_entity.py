from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime



class UserEntity:
    # initialize class members to none
    username = password = date_joined = None

    # empty constructor
    def __init__(self, username=None, password=None, date_joined=None):
        self.username, self.password, self.date_joined \
            = username, password, date_joined

    # the below are convenience methods for converting entity to/from dictionaries

    def to_dict(self):
        return {
            "usernmame": self.username,
            "password": self.password,
            "date_joined": self.date_joined
        }

    def from_dict(self, dictionary):
        if not (type(dictionary) is dict):
            raise "Requires dict as input"
        if 'username' in dic and 'password' in dic and 'date_joined' in dic:
            self.username, self.password, self.date_joined \
                = username, password, date_joined
        else:
            raise "Dictionary in UserEntity: missing required fields "


