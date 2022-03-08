import sqlite3
from flask import g
from src.const import DB_FULLPATH, DB_NAME


def init_db():
    # create or open database file
    try:
        con = sqlite3.connect(DB_FULLPATH)
        print('Connected to sqlite:' + DB_NAME)
    except Exception as e:
        print('Error opening database file: ', DB_FULLPATH)
        quit()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_FULLPATH)
    return db


def db_exec(sql, values=None):
    init_db()
    con = get_db()
    cur = con.cursor()
    if values is None:
        cur.execute(sql)
    else:
        cur.execute(sql, values)
    count = cur.rowcount
    cur.commit()
    cur.close()
    return count
