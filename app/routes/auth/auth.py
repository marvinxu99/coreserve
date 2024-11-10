from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app.utils import send_confirmation_email, confirm_token
from app.services import create_user, verify_password, get_user_by_email

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user:
            flash("Email is already registered.")
            return redirect(url_for("auth.login"))
        
        # Save user to database here (e.g., add_user(new_user))
        new_user = create_user(
            email=form.email.data, 
            password=form.password.data
        )

        if new_user:
            current_app.logger.info(f'New user created: email={new_user.email}, user_id={new_user.user_id}')
            return redirect(url_for("auth.login"))
        else:
            error = f"User {form.email.data} could not be created."
            current_app.logger.error(error)

        send_confirmation_email(form.email.data)
        flash("A confirmation email has been sent to your email address.")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)

@auth_bp.route("/confirm/<token>")
def confirm_email(token):
    email = confirm_token(token)
    if not email:
        flash("The confirmation link is invalid or has expired.", "danger")
        return redirect(url_for("auth.login"))
    
    # Update the user to set is_confirmed to True in the database
    user = User.get(email)
    if user and not user.is_confirmed:
        user.is_confirmed = True
        
        # Update user confirmation status in database

    flash("Your account has been confirmed.", "success")
    return redirect(url_for("auth.login"))

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print('here')

    if form.validate_on_submit():
        print('here2')
        user = verify_password(form.email.data, form.password.data)
        
        if user:
            login_user(user)
            return redirect(url_for("home.index"))
        
        flash("Invalid email or password.")

    return render_template("auth/login.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))