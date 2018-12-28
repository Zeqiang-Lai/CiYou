from flask import jsonify

from api.resources.base import AuthResource


class BookList(AuthResource):

    def get(self):
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


class Book(AuthResource):
    def get(self, book_id):
        pass
