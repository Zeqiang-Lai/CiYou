from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/login')
def login():
    return "login"


@auth_blueprint.route('/register')
def register():
    return "register"

