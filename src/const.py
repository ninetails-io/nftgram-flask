from os import path

DB_NAME = 'nftgram.db'
ENV = 'development'
DB_USERS = [('adam', 'a1234'), ('jason', 'j1234'), ('sean', 's1234'), ('steve', 't1234')]
DB_PROFILES = [('adam', 'Adam Kohler', "The Dude", 'The Dude Abides', "")]
APP_DIRECTORY = path.abspath(path.dirname(path.dirname(__file__)))
DB_DIRECTORY = APP_DIRECTORY + "/database/"
DB_FULLPATH = DB_DIRECTORY + DB_NAME
