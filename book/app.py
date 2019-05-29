from flask import Flask

from book.rest import book
from book.flask_settings import DevConfig

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(book.blueprint)
    return app
