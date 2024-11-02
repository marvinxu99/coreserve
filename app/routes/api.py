from flask import Blueprint, jsonify

# Define the blueprint
api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/ping', methods=['GET'])
def ping():
    """
    Health check endpoint to ensure the server is running.
    """
    return jsonify({"message": "pong"}), 200