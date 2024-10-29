from flask import Flask
from .extensions import db, migrate
from .routes import api_bp
from .config import Config

def create_app(config_class=Config):
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    return app