import os

from api import app
from api import db

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()

    app.run(host='0.0.0.0', port=5001)
