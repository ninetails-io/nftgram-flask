""" Flask configuration """
from os import environ, path
import dotenv
import src.const

# enable retrieving secrets from environment
basedir = path.abspath(path.dirname(__file__))
print("basedir = " + basedir)
dotenv.load_dotenv(path.join(basedir, '.env'))


# Base config
class Config:
    # Controls flask debug output
    TESTING = False
    DEBUG = False

    # TODO (per user) should export SECRET_KEY in .env file and use "environ.get('secret key')" below
    SECRET_KEY = 'shhhhhh!'

    # SQLITE
    DB_NAME = src.const.DB_NAME

    # JSONify
    JSONIFY_PRETTYPRINT_REGULAR = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
