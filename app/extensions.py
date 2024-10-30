# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth

db = SQLAlchemy()
migrate = Migrate()
oauth = OAuth()

def init_oauth(app):
    """
    Initialize OAuth with the given Flask app instance.
    """
    oauth.init_app(app)

    print(app.config['GOOGLE_CLIENT_ID'], app.config['GOOGLE_CLIENT_SECRET'])

    google = oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],  # Get from config
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],  # Get from config
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',  # This includes the jwks_uri
        api_base_url='https://www.googleapis.com/oauth2/v1/',
        client_kwargs={'scope': 'openid profile email'},
    )
    return google