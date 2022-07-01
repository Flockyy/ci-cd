# __init__.py

import os
import logging
from logging import StreamHandler

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_dance.contrib.google import make_google_blueprint

db = SQLAlchemy()
login_manager = LoginManager()

client_id = os.getenv('GOOGLE_CLIENT_ID')
client_secret = os.getenv('GOOGLE_CLIENT_SECRET')

blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=['profile', 'email']
)

def create_app():
    
    """Construct the core app object."""
    
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes, auth

        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
        os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

        streamHandler = StreamHandler()
        
        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)
        app.logger.addHandler(streamHandler)
        app.logger.setLevel(logging.DEBUG)
        app.register_blueprint(blueprint, url_prefix="/login")
        
        # Create Database Models
        db.create_all()

        return app