from flask import Flask

app = Flask(__name__)


def setup_flask_app():
    from controllers.identity_controller.auth_controller import auth_module
    from controllers.chat_node_controller.chat_controller import chat_module
    app.register_blueprint(auth_module)
    app.register_blueprint(chat_module)
    return app