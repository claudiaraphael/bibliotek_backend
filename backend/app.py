from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger

# import data models

# create app
def create_app():
    """
    Creates and configures the Fllask application with OpenAPI3.0 integrated.
    """

    info = {
        'title': 'Bibliotek',
        'version': '1.0',
        'description': 'Bibliotek is an open-source online library created with public domain books for students to access. It also contains an online PDF reader with markers. The project was built with Flask, Swagger for documentation and vanilla JavaScript on the frontend.',        
    }

    # create flask application instance
    app = Flask(__name__)

    # SQLAlchemy config
    app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite:///truthlable.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Swagger config
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }