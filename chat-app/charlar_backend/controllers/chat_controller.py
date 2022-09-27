from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

chat_module = Blueprint("chat_module", __name__, url_prefix="/chat")


@jwt_required()
@chat_module.route("/", methods=['GET'])
def chat_app_info():
    """
    discription: ping route for chat controller
    :return:
    """
    return jsonify({
        "app-name": "Charlar",
        "contoller": "chat",
        "info": __name__
    }), 200