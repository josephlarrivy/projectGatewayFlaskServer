import os
from flask import Flask
from routes.test_routes import test_blueprint


app = Flask(__name__)

app.register_blueprint(test_blueprint, url_prefix='/test')

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug=True)