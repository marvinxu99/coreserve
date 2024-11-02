from flask import Blueprint, request, jsonify
from app.resources.patient import Patient
from app.services.fhir_service import FHIRService

patient_bp_r4 = Blueprint('patient_bp_r4', __name__, url_prefix="/fhir/r4")
fhir_service = FHIRService()


@patient_bp_r4.route('/Patient', methods=['POST'])
def create_patient():
    data = request.json
    
    patient = Patient.from_dict(data)

    fhir_service.save_resource(patient)
    return jsonify(patient.to_dict()), 201


@patient_bp_r4.route('/Patient/<id>', methods=['GET'])
def get_patient(id):
    patient = fhir_service.get_resource('Patient', id)
    if patient:
        return jsonify(patient.to_dict())
    return jsonify({"error": "Patient not found"}), 404


@patient_bp_r4.route('/Patient/<id>', methods=['PUT'])
def update_patient(id):
    data = request.json
    updated_patient = Patient.from_dict(data)
    result = fhir_service.update_resource('Patient', id, updated_patient)
    return jsonify(result.to_dict()) if result else (jsonify({"error": "Patient not found"}), 404)


@patient_bp_r4.route('/Patient/<id>', methods=['DELETE'])
def delete_patient(id):
    success = fhir_service.delete_resource('Patient', id)
    return jsonify({"message": "Patient deleted"} if success else {"error": "Patient not found"}), 200
