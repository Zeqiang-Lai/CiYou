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
        return BookModel(book_id)

    def get_username(self):
        return self.db_model.username

    def get_booklist(self):
        """
        :return:
        :rtype: BookModel
        """
        # TODO:
        booklist = [BookModel(1), BookModel(2)]
        return booklist

    def get_checkin_info(self, year, month):
        # TODO:
        pass

    def checkin(self, year, month, day):
        # TODO:
        return True

    def get_least_history(self, num_of_days):
        # TODO:
        plan = [100, 200, 300, 500, 200, 150, 100, 200, 300]
        done = [100, 190, 150, 490, 140, 150, 80, 180, 250]
        return {
            "plan": plan,
            "done": done
        }

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
