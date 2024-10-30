from flask import Blueprint, session, redirect, url_for, jsonify
from app.extensions import init_oauth

# Create an authentication blueprint
auth_bp = Blueprint('auth', __name__)

def register_oauth_routes(app):
    # Initialize OAuth with the app context
    google = init_oauth(app)

    @auth_bp.route('/login')
    def login():
        # Create the redirect URI for the authorization callback
        redirect_uri = url_for('auth.authorize', _external=True)
        return google.authorize_redirect(redirect_uri)

    @auth_bp.route('/authorize')
    def authorize():
        # Get access token from Google
        token = google.authorize_access_token()  # This validates the state parameter automatically
        if token is None:
            return jsonify({"error": "Authorization failed!"}), 401

        # Fetch user information
        resp = google.get('userinfo')
        if resp.status_code != 200:
            return jsonify({"error": "Failed to fetch user info!"}), 400
        
        user_info = resp.json()

        # Store user email and id in session
        session['email'] = user_info['email']
        session['id'] = user_info['id']
        session.permanent = True  # Make the session permanent
        return redirect('/index')

    @auth_bp.route('/logout')
    def logout():
        # Clear user session data
        session.pop('email', None)
        session.pop('id', None)
        return redirect('/')

    # Register the blueprint
    app.register_blueprint(auth_bp)

    # Attach OAuth client to the app context for use in other views if needed
    app.extensions['google_oauth'] = google
