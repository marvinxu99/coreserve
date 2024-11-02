from .r4.patient import patient_bp_r4
from .r5.patient import patient_bp_r5

def register_fhir_routes(app):
    app.register_blueprint(patient_bp_r4)
    app.register_blueprint(patient_bp_r5)
