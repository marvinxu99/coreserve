from flask import Blueprint, session, redirect, url_for, jsonify, g
from app.extensions import init_oauth
from flask_login import login_user, current_user, logout_user
from app.services import get_user_by_email, create_user


# Create an authentication blueprint
auth_bp = Blueprint('oauth1', __name__)

def register_o_auth_routes(app):
    # Initialize OAuth with the app context
    google = init_oauth(app)

    @auth_bp.route('/login')
    def login():
        # Create the redirect URI for the authorization callback
        redirect_uri = url_for('oauth1.authorize', _external=True)
        return google.authorize_redirect(redirect_uri)

    @auth_bp.route('/authorize')
    def authorize():
        # Get access token from Google
        token = google.authorize_access_token()  # This validates the state parameter automatically
        if token is None:
            return jsonify({"error": "Authorization failed!"}), 401

        # Fetch user information
        response = google.get('userinfo')
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch user info!"}), 400
        
        user_info = response.json()

        # Store user email and id in session
        session['email'] = user_info['email']
        session['id'] = user_info['id']
        session['access_token'] = token['access_token']
        session.permanent = True  # Make the session permanent
        print(token['access_token'])

        # save user to database if not saved already.
        user = get_user_by_email(user_info['email'])
        if not user:
            # Save user to database here
            user = create_user(
                email=user_info['email'],
                password='randonpassword'
            )

        login_user(user)
        g.user = current_user

        return redirect('/index')


    @auth_bp.route('/logout')
    def logout():
        # Clear user session data
        session.pop('email', None)
        session.pop('id', None)

        logout_user()
        g.user = None

        return redirect('/')

    # Register the blueprint
    app.register_blueprint(auth_bp)

    # Attach OAuth client to the app context for use in other views if needed
    app.extensions['google_oauth'] = google
