# this is a static class which handles crud operations in the database
# it is currently set up to run SQLite, but with a little modification, will work with other RDBMS types

from werkzeug.security import generate_password_hash, check_password_hash
from src.sql_statements import CREATE_SQL, READ_SQL, UPDATE_SQL, DELETE_SQL
from src.db import get_db, db_exec
from src.tools import to_dict, to_dict_array

class CRUD:

    # performs a single create operation, returning a True if successful or False on failure
    @staticmethod
    def create(entityname, values):
        count = db_exec(UPDATE_SQL[entityname], values)
        result = False if count <= 0 else True
        print("Create of " + entityname + " with " + + values[0] + "(success=" + result + ")")
        return result

    # performs a single-row read operation, returning a dict of successful or None if not found
    @staticmethod
    def read(entityname, values):
        cur = get_db().cursor()
        result = cur.execute(CREATE_SQL[entityname], values)
        count = result.rowcount
        if count <= 0:
            row = None
            print("Read of " + entityname + " with " + values[0] + " failed")
        else:
            row = to_dict(result.description, result.fetchone())
            return row

    # performs a single update operation, returning True if successful or False if not found
    @staticmethod
    def update(entityname, values):
        count = db_exec(UPDATE_SQL[entityname], values)
        result = False if count <= 0 else True
        print("Update of " + entityname + " with " + + values[0] + "(success=" + result + ")")
        return result

    @staticmethod
    def delete(entityname, values):
        count = db_exec(UPDATE_SQL[entityname], values)
        result = False if count <= 0 else True
        print("Delete of " + entityname + " with " + + values[0] + "(success=" + result + ")")
        return result



