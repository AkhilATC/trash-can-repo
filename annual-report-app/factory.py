from flask import Flask


app = Flask(__name__)


def create_app():
    # return flask app object
    from controller.data_interface import data_layer
    app.register_blueprint(data_layer)
    return app

