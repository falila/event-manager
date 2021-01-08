from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_restful import Api
from resources.errors import errors


app = Flask(__name__)
app.config.from_pyfile('settings.py')
mail = Mail(app)


api = Api(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
app.debug = True
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
    'host': 'localhost:27017'
}
from db.db import initialize_db

initialize_db(app)
from resources.routes import initialize_routes

initialize_routes(api)
