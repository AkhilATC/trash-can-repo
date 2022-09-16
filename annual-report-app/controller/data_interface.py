from flask import Blueprint, request, jsonify

data_layer = Blueprint('data_layer', __name__, url_prefix="/data")


@data_layer.route('/', methods=['GET'])
def fetch_annual_data():
    """

    :return:
    """
    args = request.args.get('well')
    if args:

        return jsonify({
            'oil': 1,
            'gas': 1,
            'brine': 1
        })
    return jsonify({'message':"can't fetch data invalid inputs"}), 400