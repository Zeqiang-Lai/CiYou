from flask import jsonify

from api.models.book import BookModel
from api.models.database import UserDBModel


class UserModel:

    def __init__(self, db_model):
        """
        :type db_model: UserDBModel
        :param db_model:
        """
        self.db_model = db_model

    def verify_password(self, password):
        return self.db_model.verify_password(password)

    def generate_auth_token(self, expiration=6000):
        return self.db_model.generate_auth_token(expiration)

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
        user_db_model = UserDBModel.verify_auth_token(token)
        if user_db_model is not None:
            return UserModel(user_db_model)

    @staticmethod
    def verify_email(email):
        user_db_model = UserDBModel.query.filter_by(email=email).first()
        if user_db_model is not None:
            return UserModel(user_db_model)

    @staticmethod
    def register(email, username, password):
        UserDBModel.register(email, username, password)
