from flask import (Blueprint, render_template, redirect, url_for, 
                   flash, current_app, g, request, abort)
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegistrationForm, LoginForm
from app.utils import send_confirmation_email, confirm_token
from app.services import create_user, verify_password, get_user_by_email, update_user
from urllib.parse import urlparse   # For safer URL validation

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = get_user_by_email(form.email.data)
        if user:
            flash("Email is already registered.")
            return redirect(url_for("auth.login"))
        
        # Save user to database here
        new_user = create_user(
            email=form.email.data, 
            password=form.password.data
        )
        if new_user:
            current_app.logger.info(f'New user created: email={new_user.email}, user_id={new_user.user_id}')
            send_confirmation_email(form.email.data)
            flash("A confirmation email has been sent to your email address.")
            return redirect(url_for("auth.login"))
        else:
            error = f"User {form.email.data} could not be created."
            current_app.logger.error(error)
            flash(error)

    return render_template("auth/register.html", form=form)


@auth_bp.route("/confirm/<token>")
def confirm_email(token):
    email = confirm_token(token)
    if not email:
        flash("The confirmation link is invalid or has expired.", "danger")
        return redirect(url_for("auth.login"))
    
    # Update the user to set is_confirmed to True in the database
    user = get_user_by_email(email)
    if user and not user.is_confirmed:
        update_user(user_id=user.user_id, is_confirmed=True)

    flash("Your account has been confirmed.", "success")
    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = verify_password(form.email.data, form.password.data)
        if user:
            login_user(user)
            g.user = current_user

            next_url = request.args.get('next')
            # url_has_allowed_host_and_scheme should check if the url is safe
            # for redirects, meaning it matches the request host.
            # See Django's url_has_allowed_host_and_scheme for an example.
            if not url_has_allowed_host_and_scheme(next_url, request.host_url):
                return abort(400)
        
            return redirect(next_url or url_for("home.index"))
        
        flash("Invalid email or password.")

    return render_template("auth/login.html", form=form)

def url_has_allowed_host_and_scheme(url, host_url):
    """Check if the URL is safe for redirection."""
    if not url:
        return True
    
    parsed_url = urlparse(url)
    host_netloc = urlparse(host_url).netloc
    return parsed_url.scheme in ("http", "https") and parsed_url.netloc == host_netloc


@auth_bp.route("/logout")
def logout():
    logout_user()
    g.user = None
    return redirect(url_for("home.index"))