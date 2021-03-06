from api.models.book import BookModel
from api.models.database import UserDBModel


class UserModel:

    def __init__(self, user_db_model):
        """
        :type db_model: UserDBModel
        :param db_model:
        """
        self.user_db_model = user_db_model

    def verify_password(self, password):
        return self.user_db_model.verify_password(password)

    def generate_auth_token(self, expiration=6000):
        return self.user_db_model.generate_auth_token(expiration)

    def find_book_by_id(self, book_id):
        # TODO:
        return BookModel(book_id)

    def get_username(self):
        return self.user_db_model.username

    def get_booklist(self):
        """
        :return:
        :rtype: BookModel
        """
        # TODO:
        booklist = [BookModel(1), BookModel(2)]
        return booklist

    def get_checkin_info(self, year, month):
        """
        获取该年该月的签到信息
        :param year:
        :param month:
        :return: 一个list,包含该月所有签到的天,格式如下
        [
            {
                "year": int
                "month": int
                "day": int
            },
            ...
        ]
        """
        # TODO:
        checkin_info = [
            {
                'year': 2018,
                'month': 12,
                'day': 1
            },
            {
                'year': 2018,
                'month': 12,
                'day': 2
            },
            {
                'year': 2018,
                'month': 12,
                'day': 15
            }
        ]
        return checkin_info

    def checkin(self, year, month, day):
        """
        签到,需写入数据库
        :param year:
        :param month:
        :param day:
        :return: 返回是否签到成功
        """
        # TODO:
        return True

    def get_least_history(self, num_of_days):
        """
        获取最近的背词记录
        :param num_of_days: 要获取的天数,从今天开始往前倒退
        :return: 一个字典,格式如下
        {
            "plan": plan, # 计划背诵单词量
            "done": done  # 实际完成量
        }
        """
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
