from flask_restful import Resource
from flask import jsonify

class BookList(Resource):

    def get(self):
        return jsonify([
            {
                "name": "Book1",
                "description": "Description1"
            },
            {
                "name": "Book2",
                "description": "Description2"
            }
        ])


