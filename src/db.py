import sqlite3
from flask import g
from src.const import DB_FULLPATH


def init_db():
    # create or open database file
    try:
        con = sqlite3.connect(DB_DIRECTORY + DB_NAME)
        print('Connected to sqlite:' + DB_NAME)
    except Exception as e:
        print('Error opening database file: ', DB_FULLPATH)
        quit()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_FULLPATH)
    return db
