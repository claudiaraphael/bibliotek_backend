from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from extensions import db

# import data models

# create app
def create_app():
    """
    Creates and configures the Fllask application with OpenAPI3.0 integrated.
    """
    # metadata
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

    swagger_template = {
        "info": {
            "title": "Bibliotek",
            "description": "Open-source library project with public domain books built with flask.",
            "version": "1.0",
        },
        "schemes": ["http"],
        "tags": [
            {
                "name": "Book",
                "description": "Operações relacionadas a produtos"
            },
            {
                "name": "User",
                "description": "Operações relacionadas a usuários"
            },
            
        ]
    }

    # Inicializar Swagger
    Swagger(app, config=swagger_config, template=swagger_template)

    # db.init_app(app) initializes the SQLAlchemy database with the Flask app
    db.init_app(app)

    # CORS Configuration: connect front end to back end
    CORS(app, resources={
        r"/*": {
            "origins": ["http://127.0.0.1:5500"],  # Frontend origin
            "methods": ["GET", "POST", "PUT", "DELETE", "PATCH"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    