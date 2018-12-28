from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# from api.resources.user import User

from api.routes.auth import auth_blueprint

app = Flask(__name__)
app.debug = True

app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/myapi'

# api = Api(app)
# db = SQLAlchemy(app)

# api.add_resource(User, '/user')

