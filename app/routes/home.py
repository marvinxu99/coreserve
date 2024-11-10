from flask import Blueprint, session, render_template
from app.services import uar_get_code_by
from flask_login import current_user

# Define the blueprint
home_bp = Blueprint('home', __name__)


# a simple page that says hello
@home_bp.route('/')
@home_bp.route('/index')
def index():
    # If logged in, show the user's email and id
    # session_d = dict(session)
    # email = session_d.get('email', None)
    # id = session_d.get('id', None)
    email = current_user.email
    id =current_user.user_id
    code = uar_get_code_by("DISPLAY", 48, "Active")
    
    return f'Hello, email={email}, id={id}, code={code}!'


@home_bp.route('/react')
def test_react():
    return render_template('test_react/index.html')

