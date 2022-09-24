from flask import Blueprint, request, jsonify

auth_module = Blueprint("auth_module", __name__, url_prefix="/auth")


@auth_module.route("/", methods=['GET'])
def auth_app_info():
    """
    discription: ping route for chat controller
    :return:
    """
    return jsonify({
        "app-name": r"Charlar",
        "contoller": "Auth",
        "info": __name__
    }), 200