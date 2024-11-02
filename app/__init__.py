import os
from datetime import timedelta
from flask import Flask
from .extensions import db, migrate, cache
from .routes import register_routes
from app.config import config
from app.services import create_global_cv_dicts
from app.commands import register_commands

from app import models  # This registers all models with SQLAlchemy


def create_app(config_name="development"):
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Use the secret key for session management
    app.secret_key = app.config['SECRET_KEY']
    
    # Set session expiration to automatically clear the session after a certain time period
    app.permanent_session_lifetime = timedelta(minutes=10)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
   
    # Register Blueprints
    register_routes(app)

    # Register the CLI command
    register_commands(app)
    
    # Create dicts for uar_get functions
    with app.app_context():
        create_global_cv_dicts()          # This is now safe within the app context
   
    return app