from src.db import init_db, get_db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlite

# this class performs CRUD operations using UserEntity objects



class DB_User:

    def db_create(self, user):
        try:
            # execute an INSERT query to add new data
            query = "INSERT OR IGNORE INTO users VALUES (?,?,?,?) RETURNS *"
            values = (self.id, self.username, self.password, self.date_joined)
            cur = get_db().cursor()
            
            result = cur.execute(query, values)
            print(result.fetchone())

            get_db().commit()
            get_db().close()
        except sqlite3.Error as e:
            self.record_status = -1
        except Exception as e:
            # unknown error
            self.record_status = -1

    @staticmethod
    def db_read(self, username):
        try:
            # execute a select query to retrieve the record by username
            query = 'SELECT * FROM users WHERE username=?'
            values = (username,)
            cur = get_db().cursor()
            result = get_db().cursor().execute(query, (username,))
            get_db().close()

            # convert to dict and record results
            user = to_dict(result.description, result.fetchone())
            self.id, self.username, self.password, self.date_joined, self.status = \
                user["id"], user["username"], user["password"], user["date_joined"], 1

        # error handlers
        except sqlite3.DatabaseError as e:
            self.status = -1
        except sqlite3.ProgrammingError as e:
            self.status = -1
        except sqlite3.Error as e:
            self.status = -1
        except Exception as e:
            self.status = -1
