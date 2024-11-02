import os
from datetime import timedelta
from flask import Flask, session
from sqlalchemy import inspect
from .extensions import db, migrate, cache
from .routes import (
    api_bp, 
    register_oauth_routes, 
    patient_bp 
)
from app.config import config
from app.services.db_uar_service import create_global_cv_dicts
from app.commands import init_code_set, db_fix

from app.services.db_uar_service import uar_get_code_by


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
    # cache.init_app(app)

    # Import models here to make sure they're registered
    from app.models.code_value_set import CodeSet
    from app.models.code_value import CodeValue
    from app.models.user import Users

    # a simple page that says hello
    @app.route('/')
    @app.route('/index')
    def index():
        # If logged in, show the user's email and id
        session_d = dict(session)
        email = session_d.get('email', None)
        id = session_d.get('id', None)
        code = uar_get_code_by("DISPLAY", 48, "Active")
        return f'Hello, email={email}, id={id}, code={code}!'
    
    # Register Blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    register_oauth_routes(app)
    app.register_blueprint(patient_bp)

    # Register the CLI command
    app.cli.add_command(init_code_set)
    app.cli.add_command(db_fix)
    
    # Create dicts for uar_get functions
    with app.app_context():
        create_global_cv_dicts(db)          # This is now safe within the app context
        print(db.get_engine().url)
        engine = db.get_engine()
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("Tables in the coreserve1 database: ", tables)

   
    return app