from flask import Blueprint

test_blueprint = Blueprint('test', __name__)

@test_blueprint.route("/testGateway")
def test_gateway():
  return "Hitting Flask API via Gateway"