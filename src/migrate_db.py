import sqlite3
from os import path, getcwd
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from src.const import DB_FULLPATH, DB_USERS

# Create the SQLite database file and populate it with test users
def init_db():
    print("WORKING_DIR = " + path.dirname(getcwd()))
    print("DB_FULLPATH = " + DB_FULLPATH)

    try:
        con = sqlite3.connect(DB_FULLPATH)
        print('Connected to sqlite:' + os.path.basename(DB_FULLPATH))
    except Exception as e:
        print('Unable to create database file ' + os.path.basename(DB_FULLPATH))
        quit();

    # Get a cursor object needed to execute queries
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute('CREATE TABLE IF NOT EXISTS users(user_id text PRIMARY KEY, password text, date_joined Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')

    # Parameterized SQL Query String for adding users
    query = "INSERT OR IGNORE INTO users VALUES (?,?,?)"

    # Insert users
    for user in DB_USERS:

        # get values to be inserted
        id = user[0]
        pw = generate_password_hash(user[1])
        dt = datetime.utcnow()
        values = (id, pw, dt)

        try:
            cur.execute(query, values)
            print("Success: Added user ", id, " pw="+pw)
        except:
            print('Error: Unable to add user ', values)

    # commit changes to the database and close the connection
    con.commit()
    con.close()
