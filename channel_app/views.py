import os
import logging
from flask import Flask, jsonify, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from dotenv import load_dotenv
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from logging import StreamHandler

load_dotenv(override=True)

app = Flask(__name__, template_folder='../templates')

client_id = os.getenv('GOOGLE_CLIENT_ID')
client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
app.secret_key=os.getenv('secret_key')

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=['profile', 'email']
)

streamHandler = StreamHandler()
app.logger.addHandler(streamHandler)
app.logger.setLevel(logging.DEBUG)
app.register_blueprint(blueprint, url_prefix="/login")

login_manager = LoginManager()
login_manager.init_app(app)

@app.after_request
def after_request(response):
    # appinsights.flush()
    return response

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

@app.route('/')
def index():
    # Test of app.logger
    app.logger.debug('This is a debug log message')
    app.logger.info('This is an information log message')
    app.logger.warn('This is a warning log message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')
    
    # Google endpoint
    google_data = None
    user_info_endpoint='/oauth2/v2/userinfo'

    if google.authorized:
        google_data = google.get(user_info_endpoint).json()
    
    return render_template('base.html',
        google_data = google_data,
        fetch_url = google.base_url+user_info_endpoint
    )

@app.route('/login')
def login():
    return redirect(url_for('google.login'))

@app.route('/logout')
def logout():
    token = blueprint.token["access_token"]
    resp = google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert resp.ok, resp.text
    del blueprint.token
    return redirect(url_for('index'))