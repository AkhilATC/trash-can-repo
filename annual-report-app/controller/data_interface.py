from flask import Blueprint, request, jsonify
import pandas as pd

data_layer = Blueprint('data_layer', __name__, url_prefix="/data")


@data_layer.route('/', methods=['GET'])
def fetch_annual_data():
    """

    :return:
    """
    well_id = request.args.get('well')
    if well_id:
        # read xlx file
        file_ = r'data/input.xls'
        df = pd.read_excel(file_)
        df.columns = [c.replace(' ', '_') for c in df.columns]
        # filter out based on input well id
        filtered_data = df.loc[df['API_WELL__NUMBER'] == int(well_id)]
        oil_sum = int(filtered_data['OIL'].sum()) if filtered_data['OIL'].sum() else 0
        gas_sum = int(filtered_data['GAS'].sum()) if filtered_data['GAS'].sum() else 0
        brine_sum = int(filtered_data['BRINE'].sum()) if filtered_data['BRINE'].sum() else 0
        return jsonify({
            'oil': oil_sum,
            'gas': gas_sum,
            'brine': brine_sum
        })
    return jsonify({'message':"can't fetch data invalid inputs"}), 400