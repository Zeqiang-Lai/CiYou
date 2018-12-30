from flask import jsonify, g
from api.resources.base import AuthResource


class BookList(AuthResource):

    def get(self):
        return jsonify(g.user.get_booklist())


class BookInfo(AuthResource):
    def get(self, book_id):
        pass


class BookWords(AuthResource):
    def get(self, book_id, st_idx, length):
        pass


class ReviewWordList(AuthResource):

    def get(self, book_id, word_num):
        book_model = g.user.find_book_by_id(book_id)
        return jsonify(book_model.get_review_list(word_num))
