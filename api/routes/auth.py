from flask import Blueprint, Flask, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth


from api.models.user import UserModel

auth_blueprint = Blueprint('auth', __name__)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    # first try to authenticate by token
    user = UserModel.verify_auth_token(email_or_token)
    if not user:
        # try to authenticate with username/password
        user = UserModel.verify_email(email=email_or_token)
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
    return jsonify({
        'token': token.decode('ascii'),
        'username': g.user.get_username(),
        'duration': 6000}
    )


@auth_blueprint.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    if username is None or password is None or email is None:
        abort(400)  # missing arguments
    if UserModel.verify_email(email) is not None:
        abort(400)  # existing user

    UserModel.register(email=email,
                       username=username,
                       password=password)

    return jsonify({'username': username,
                    'email': email}), 201
