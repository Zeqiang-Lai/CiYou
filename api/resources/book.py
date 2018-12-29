from flask import jsonify, g
from api.resources.base import AuthResource


class BookList(AuthResource):

    def get(self):
        return g.user.get_booklist()


class Book(AuthResource):
    def get(self, book_id):
        pass
