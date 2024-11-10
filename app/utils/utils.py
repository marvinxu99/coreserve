from flask_mail import Message
from flask import url_for, render_template, current_app
from app.extensions import mail, serializer
from itsdangerous import URLSafeTimedSerializer

def generate_confirmation_token(email):
    return serializer.dumps(email, salt="email-confirm")

def send_confirmation_email(user_email):
    token = generate_confirmation_token(user_email)
    confirm_url = url_for("auth.confirm_email", token=token, _external=True)
    html = render_template("auth/confirm_email.html", confirm_url=confirm_url)
    subject = "Please confirm your email"
    
    msg = Message(subject, recipients=[user_email], html=html)
    mail.send(msg)

# Token generator for email confirmation
def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.secret_key)
    return serializer.dumps(email, salt="email-confirm")

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.secret_key)
    try:
        email = serializer.loads(token, salt="email-confirm", max_age=expiration)
    except Exception:
        return False
    return email