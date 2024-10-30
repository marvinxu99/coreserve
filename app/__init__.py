import os
from datetime import timedelta
from flask import Flask, session
from .extensions import db, migrate
from .routes import api_bp, register_oauth_routes
from .config import Config


def create_app(config_class=Config):
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

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

    # a simple page that says hello
    @app.route('/')
    @app.route('/index')
    def index():
        # If logged in, show the user's email and id
        session_d = dict(session)
        email = session_d.get('email', None)
        id = session_d.get('id', None)
        return f'Hello, email={email}, id={id}!'
    
    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    register_oauth_routes(app)

    return app