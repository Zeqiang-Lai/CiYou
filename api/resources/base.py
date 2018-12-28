from api.routes.auth import auth
from flask_restful import Resource


class AuthResource(Resource):
    method_decorators = [auth.login_required]