from flask import jsonify
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from api import db
from api.models.book import BookModel

SECRET_KEY = 'the quick brown fox jumps over the lazy dog'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), index=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    def find_book_by_id(self, book_id):
        # TODO:
        return BookModel()

    def get_booklist(self):
        # TODO:
        return jsonify([
            {
                "id": 1,
                "name": "Book1",
                "description": "Description1"
            },
            {
                "id": 2,
                "name": "Book2",
                "description": "Description2"
            }
        ])

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user


