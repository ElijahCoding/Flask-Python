# export FLASK_APP=GuestBook
from flask import *

def create_app():
    app = Flask(__name__)

    from .views import main

    app.register_blueprint(main)

    return app