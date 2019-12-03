# export FLASK_APP=GuestBook
from flask import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:8889/fresh'

    from .views import main
    app.register_blueprint(main)

    return app