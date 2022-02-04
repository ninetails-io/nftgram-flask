import sqlite3
from flask import g

import src.const

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(src.const.DB_NAME)
    return db