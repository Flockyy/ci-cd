"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_dance.contrib.google import google
from . import blueprint

# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

# @main_bp.route("/", methods=["GET"])
# @login_required
# def dashboard():
#     """Logged-in User Dashboard."""
#     return render_template(
#         "dashboard.jinja2",
#         title="Flask-Login Tutorial",
#         template="dashboard-template",
#         current_user=current_user,
#         body="You are now logged in!",
#     )

@main_bp.route('/', methods=["GET"])
def index():
    # Google endpoint
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'

    if google.authorized:
        google_data = google.get(user_info_endpoint).json()
    
    return render_template('base.html',
        google_data = google_data,
        fetch_url = google.base_url+user_info_endpoint
    )
    
@main_bp.route('/google_login', methods=['GET', 'POST'])
def google_login():
    return redirect(url_for('google.login'))

@main_bp.route("/logout")
# @login_required
def logout():
    """User log-out logic."""
    token = blueprint.token["access_token"]
    resp = google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert resp.ok, resp.text
    del blueprint.token
    logout_user()
    return redirect(url_for('main_bp.index'))
