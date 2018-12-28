from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cors = CORS(app, resources={r"/*": {"origins":"*"}})

db = SQLAlchemy(app)

from api.routes.auth import auth_blueprint

app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

from api.resources.book import BookList
from api.resources.word import ReviewWordList, Word

api = Api(app)
api.add_resource(BookList, '/api/resources/book')
api.add_resource(ReviewWordList, '/api/resources/review_words/<int:book_id>/<int:word_num>')
api.add_resource(Word, '/api/resources/word/<int:book_id>/<string:word_spell>')