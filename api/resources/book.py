from flask import jsonify, g
from api.resources.base import AuthResource

from api.models.book import BookModel


class BookList(AuthResource):

    def get(self):
        book_list = []
        books = g.user.get_booklist()
        for book in books:
            book_list.append(book.get_info())
        return book_list


class BookInfo(AuthResource):
    def get(self, book_id):
        book = g.user.find_book_by_id(book_id)
        if book is not None:
            return book.get_info()
        else:
            return 404


class BookWords(AuthResource):
    def get(self, book_id, st_idx, length):
        book = g.user.find_book_by_id(book_id)
        if book is not None:
            word_list = []
            words = book.get_word_list(st_idx, length)
            for word in words:
                word_list.append(word.get_info())
            return word_list
        else:
            return 404


class ReviewWordList(AuthResource):

    def get(self, book_id, word_num):
        book = g.user.find_book_by_id(book_id)
        if book is not None:
            return book.get_review_list(word_num)
        else:
            return 404
