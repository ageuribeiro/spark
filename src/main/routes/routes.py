from flask import Blueprint, request, jsonify

# Import the request_adapter function from the adapters module
from src.main.adapters.request_adapter import request_adapter

# Import the user_finder_composer and user_register_composer functions from the composers module
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer

# Import the user_finder_validator and user_register_validator functions from the validators module
from src.validators.user_register_validator import user_register_validator
from src.validators.user_finder_validator import user_finder_validator

# Import the handle_errors function from the error_handler module
from src.errors.error_handler import handle_errors


user_route_bp = Blueprint("user_routes", __name__)


@user_route_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = None

    try:
        user_finder_validator(request)
        http_response = request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/user", methods=["POST"])
def register_user():
    http_response = None

    try:
        user_register_validator(request)
        http_response = request_adapter(request, user_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code    
