from flask import Flask


app = Flask(__name__)

# return flask app object


def create_app():
    from controller.data_interface import data_layer
    app.register_blueprint(data_layer)
    return app

