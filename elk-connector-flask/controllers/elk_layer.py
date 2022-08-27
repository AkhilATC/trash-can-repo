from flask import Blueprint, current_app
import models

elk_module = Blueprint('elk_module', __name__, url_prefix="/elk")


@elk_module.route("/", methods=['GET'])
def fetch():
    """

    :return:
    """
    con = models.get_elk_connection_as_es()
    print(current_app.config['ELK_URI'])
    print(con)
    f = con.indices.exists_alias(name="demo")
    print(f"connection = {f}")
    return "Home"