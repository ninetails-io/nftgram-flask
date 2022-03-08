import sqlite3
from os import path, getcwd
import os
import textwrap
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from src.const import DB_FULLPATH, DB_USERS, DB_PROFILES
from src.sql_statements import CREATE_TABLES_SQL, CREATE_SQL
from src.db import get_db, db_exec


# Create the SQLite database file and populate it with test users
# TODO: CREATE A SQL FILE TO HANDLE ALL DATABASE CREATION TASKS

def init_db():
    print("WORKING_DIR = " + path.dirname(getcwd()))
    print("DB_FULLPATH = " + DB_FULLPATH)

    try:
        con = sqlite3.connect(DB_FULLPATH)
        print('Connected to sqlite:' + os.path.basename(DB_FULLPATH))
    except Exception as e:
        print('Unable to crate database file ' + os.path.basename(DB_FULLPATH))
        quit()

    try:
        # drop and create each database table
        for table, sql in CREATE_TABLES_SQL.items():
            if True: con.execute("DROP TABLE IF EXISTS " + table + ";")
            con.execute(sql)
    except Exception as e:
        print("Could not create all database tables")
        quit()

    # INSERT INITIAL DATA: USERS
    # Get SQL string from CREATE_SQL and add each user listed in DB_USERS
    query = CREATE_SQL['users']
    for user in DB_USERS:
        user_id = user[0]
        password = user[1]
        secured = generate_password_hash(password)
        role = "user"
        dt = datetime.utcnow()
        values = (user_id, secured, role, dt)
        try:
            count = con.execute(query, values).rowcount
            if count > 0: print("Success: Added user ", user[0], " pw=" + user[1])
        except:
            print('Error: Unable to add user ', values)
    # commit users to database
    con.commit()

    # INSERT INITIAL DATA: PROFILES
    query = CREATE_SQL['profiles']
    for profile in DB_PROFILES:
        val = (profile[0], profile[1], profile[2], profile[3], profile[4])
        try:
            count = con.execute(query, val).rowcount
            if count > 0: print("Success: Added profile for " + profile[1] + ": " + profile[2])
        except Exception as e:
            print("Error: Unable to add profile for user: " + user[0])

    # CLEAN UP
    con.close()
