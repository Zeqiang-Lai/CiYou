import os

from api import app
from api import db

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()

    app.run()
