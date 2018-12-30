from flask import Blueprint, Flask, abort, request, jsonify, g, url_for
from api.routes.auth import auth

common_blueprint = Blueprint('common', __name__)


@common_blueprint.route('/tag_word', methods=['POST'])
@auth.login_required
def tag_word():
    book_id = request.json.get('book_id')
    word_spell = request.json.get('word_spell')
    type = request.json.get('type')
    g.user.tag_word(book_id, word_spell, type)
