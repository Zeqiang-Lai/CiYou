from flask import jsonify

from api.resources.base import AuthResource
from api.models.book import BookModel
from api.models.word import WordModel


class Word(AuthResource):

    def get(self, book_id, word_spell):
        book = BookModel.find_by_id(book_id)

        return book.get_word(word_spell)


class WordList(AuthResource):
    pass


class ReviewWordList(AuthResource):

    def get(self, book_id, word_num):
        book = BookModel.find_by_id(book_id)

        return book.get_review_list(word_num)
