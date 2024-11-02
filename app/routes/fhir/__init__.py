from .patient import patient_bp 

def register_fhir_routes(app):
    app.register_blueprint(patient_bp)
