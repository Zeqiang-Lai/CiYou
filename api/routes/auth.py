from flask import Blueprint, Flask, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth


from api.models.user import User
from api import db


auth_blueprint = Blueprint('auth', __name__)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(email_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(email=email_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth_blueprint.route('/')
def index():
    return "Authorization API"


@auth_blueprint.route('/login', methods=['GET'])
@auth.login_required
def login():
    token = g.user.generate_auth_token(6000)
    return jsonify({'token': token.decode('ascii'), 'duration': 6000})


@auth_blueprint.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    if User.query.filter_by(email=email).first() is not None:
        abort(400)  # existing user
    user = User(username=username, email=email)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'username': user.username,
                    'email': user.email}), 201
