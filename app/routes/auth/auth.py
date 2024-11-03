import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, session, request, url_for, current_app
)
import bcrypt
from app.services import create_user, verify_password, get_user_by_id


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


def register_auth_routes(app):
    @auth_bp.route('/register', methods=('GET', 'POST'))
    def register():
        if request.method == 'POST':
            username    = request.form['username']
            password    = request.form['password']
            email       = request.form.get('email', '')        
            name_first  = request.form.get('name_first', '')
            name_last   = request.form.get('name_last', '')
            name_middle = request.form.get('name_middle', None)
            
            error = None

            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'

            if error is None:
                new_user = create_user(username, email, password, name_first, name_last, name_middle)
                # new_user = create_user("winter4", "winter4@example.com", "123456", "Winter4", "Xu")
                if new_user:
                    current_app.logger.info(f'New user created: username={new_user.username}, user_id={new_user.user_id}')
                    return redirect(url_for("auth.login"))
                else:
                    error = f"User {username} could not be created."
                    current_app.logger.error(error)

            flash(error)

        return render_template('auth/register.html')


    @auth_bp.route('/login', methods=('GET', 'POST'))
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            error = None

            # Use verify_password in db_user_service to check
            user = verify_password(username, password)

            if user is None:
                error = 'Incorrect username or password.'
            else:
                session.clear()
                session['user_id'] = user.user_id
                return redirect(url_for('index'))

            flash(error)

        return render_template('auth/login.html')


    @auth_bp.before_app_request
    def load_logged_in_user():
        user_id = session.get('user_id')

        if user_id is None:
            g.user = None
        else:
            # Use SQLAlchemy ORM to fetch the user
            g.user = get_user_by_id(user_id)


    @auth_bp.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('index'))


    def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return redirect(url_for('auth.login'))

            return view(**kwargs)

        return wrapped_view

    # Register the blueprint
    app.register_blueprint(auth_bp)
