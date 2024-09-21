from flask import Blueprint, jsonify, make_response
from services.rapid_sports_api_calls import TestModule




test_blueprint = Blueprint('test', __name__)





@test_blueprint.route("/testGateway")
def test_gateway():
    api_key = TestModule.do_import_test()
    
    if api_key:
        response = {
            "message": "Hitting Flask API via Gateway",
            "api_key": api_key
        }
        return make_response(jsonify(response), 200)
    else:
        error_response = {
            "error": "API key not found",
            "message": "Failed to retrieve API key from environment"
        }
        return make_response(jsonify(error_response), 500)
