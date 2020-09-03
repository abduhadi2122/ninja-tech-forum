from flask import Flask
from handlers.auth import auth_handlers
from handlers.comment import comment_handlers
from handlers.topic import topic_handlers
from models.settings import db

import logging
import sys



app = Flask(__name__)
app.register_blueprint(auth_handlers)
app.register_blueprint(topic_handlers)
app.register_blueprint(comment_handlers)


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# create tables in a database (important: this does not update tables, only creates new ones)
db.create_all()


if __name__ == '__main__':
    app.run()
