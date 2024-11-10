import os
from datetime import timedelta
from flask import Flask, g
from app.extensions import db, migrate, cache, mail, login_manager
from app.routes import register_routes
from app.commands import register_commands
from app.config import config
from app.utils import LoggingManager
from flask_login import current_user

from app import models      # This registers all models with SQLAlchemy


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

    # Initialize LoggingManager
    logging_manager = LoggingManager()
    app.logger = logging_manager.get_logger('coreserve')  # Set the app's logger

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    @app.before_request
    def before_request():
        # Set g.user to the current user
        g.user = current_user if isinstance(current_user, models.User) else None

    # Register Blueprints
    register_routes(app)

    # Register the CLI command
    register_commands(app)
       
    return app

@login_manager.user_loader
def load_user(user_id):
    try:
        return models.User.query.get(user_id)
    except Exception as e:
        return None