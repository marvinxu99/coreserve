from .basic import basic_bp
from .api import api_bp
from .auth.auth import register_auth_routes
from .auth.o_auth import register_o_auth_routes
from .fhir import register_fhir_routes


def register_routes(app):
    app.register_blueprint(basic_bp)
    app.register_blueprint(api_bp)
    register_auth_routes(app)
    register_o_auth_routes(app)
    register_fhir_routes(app)
