from flask import Blueprint, session
from app.services import uar_get_code_by

# Define the blueprint
basic_bp = Blueprint('basic_bp', __name__)


# a simple page that says hello
@basic_bp.route('/')
@basic_bp.route('/index')
def index():
    # If logged in, show the user's email and id
    session_d = dict(session)
    email = session_d.get('email', None)
    id = session_d.get('id', None)
    code = uar_get_code_by("DISPLAY", 48, "Active")
    return f'Hello, email={email}, id={id}, code={code}!'
