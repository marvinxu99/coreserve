from flask import Blueprint, session, render_template, g
from app.services import uar_get_code_by

# Define the blueprint
home_bp = Blueprint('home', __name__)


# a simple page that says hello
@home_bp.route('/')
@home_bp.route('/index')
def index():
    # If logged in, show the user's email and id
    # email = current_user.email
    # id =current_user.user_id
    # code = uar_get_code_by("DISPLAY", 48, "Active")    
    # return f'Hello, email={email}, id={id}, code={code}!'
    return render_template('index.html')


@home_bp.route('/profile')
def profile():
    if g.user.is_authenticated:
        return f"Welcome, {g.user.username}!"
    else:
        return "Please log in to view your profile."


@home_bp.route('/react')
def test_react():
    return render_template('test_react/index.html')

