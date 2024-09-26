from flask import Blueprint, jsonify, make_response, request
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

@test_blueprint.route("/processData", methods=["POST"])
def process_data():
    data = request.get_json()  # Get the JSON data from the request body
    
    if not data:
        error_response = {
            "error": "Invalid input",
            "message": "No data provided in the request body"
        }
        return make_response(jsonify(error_response), 400)

    # Example: process the data (you can customize this as needed)
    # For demonstration, let's say we want to echo the received data back
    processed_data = { 
        "received": data, 
        "message": "Data processed successfully" 
    }

    return make_response(jsonify(processed_data), 200)
