from flask_mail import Message
from flask import url_for, render_template, current_app
from app.extensions import mail
from itsdangerous import URLSafeTimedSerializer
import re


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])  # Generate tokens for email confirmation
    return serializer.dumps(email, salt="email-confirm")


def send_confirmation_email(user_email):
    try:
        token = generate_confirmation_token(user_email)
        confirm_url = url_for("auth.confirm_email", token=token, _external=True)
        html = render_template("auth/confirm_email.html", confirm_url=confirm_url)
        subject = "Please confirm your email"
        
        msg = Message(subject, recipients=[user_email], sender='admin@coreserve.io', html=html)
        mail.send(msg)
    except Exception as e:
        current_app.logger.error(f"Failed to send email: {e}")


# Token generator for email confirmation
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.secret_key)
    return serializer.dumps(email, salt="email-confirm")


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.secret_key)
    try:
        email = serializer.loads(token, salt="email-confirm", max_age=expiration)
    except Exception:
        current_app.logger.error('Failed to confirm email.')
        return False
    return email


def convert_to_key(v_str):
    return re.sub('[^0-9a-zA-Z]+', '', v_str).upper()


def is_valid_email(email):
    """Check if the provided email address is valid."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None