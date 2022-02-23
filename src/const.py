from os import path

DB_NAME = 'nftgram.db'
ENV = 'development'
SALT = 'cascadia'
DB_USERS = [('adam', 'a1234'), ('jason', 'j1234'), ('sean', 's1234'), ('steve', 't1234')]
DB_DIRECTORY = path.abspath(path.dirname(path.dirname(__file__))) + "/database/"
