from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from datetime import datetime
from factory import mongo_db
from json import dumps


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


@chat_module.route("/publish_my_note", methods=['POST'])
@jwt_required()
def publish_post():
    """

    :return:
    """
    try:
        post_info = request.json
        if not all([post_info[x] for x in post_info]):
            return jsonify({'message': 'mandatory fields missing'}), 409
        current_user = get_jwt_identity()
        time_now = datetime.utcnow()
        post_info.update({'wrote_by': current_user, 'created_on':time_now})
        mongo_db.db.chats.insert_one(post_info)
        return jsonify({'message': f"{current_user}'s post saved successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({'message':'Failed'}), 400


@chat_module.route("/fetch_posts", methods=['GET'])
@jwt_required()
def fetch_posts():
    """

    :return:
    """
    try:
        data = list(mongo_db.db.chats.find({}))
        return Response(dumps(data, default=str), mimetype='application/json')
    except Exception as e:
        print(e)
        return jsonify({'message':'Failed'}), 500