from flask import Blueprint
from flask import request
from flask import jsonify
from controller.sparql_controller import *


search_api = Blueprint('search_api', __name__)


@search_api.route('/products', methods=["GET"])
def get_all_products_route():
    restaurant = get_all_products()
    return jsonify(restaurant)


@search_api.route('/restaurants', methods=["POST"])
def get_all_restaurants_route():
    filter = request.json
    result = get_all_restaurants(filter)
    return result