from flask import g
from flask_restful import Resource

from api.resources.base import AuthResource


class Word(AuthResource):

    def get(self, book_id, word_spell):
        book_model = g.user.find_book_by_id(book_id)
        return book_model.get_word(word_spell)

class Search(Resource):
    def get(self, word_spell):
        # TODO:
        return word_spell
