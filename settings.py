from os import environ


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_ENV")
    FLASK_APP = environ.get("FLASK_APP")
