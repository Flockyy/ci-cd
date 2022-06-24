import os
from flask import Flask, jsonify, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from dotenv import load_dotenv

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

app.register_blueprint(blueprint, url_prefix="/login")

@app.route('/')
def index():
    google_data = None
    user_info_endpoint='/oauth2/v2/userinfo'
    if google.authorized:
        google_data=google.get(user_info_endpoint).json()
        
    return render_template('base.html',
        google_data = google_data,
        fetch_url=google.base_url+user_info_endpoint
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