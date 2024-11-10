from .home import home_bp
from .api import api_bp
from .auth.auth import auth_bp
from .auth.o_auth import register_o_auth_routes
from .fhir import register_fhir_routes


def register_routes(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)
    register_o_auth_routes(app)
    register_fhir_routes(app)
