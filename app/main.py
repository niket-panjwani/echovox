from flask import Flask, render_template
from app.routes.web_interface import upload_audio_blueprint
from app.auth.microsoft_auth import microsoft_auth_blueprint
from flask_cors import CORS
from flask_session import Session
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'niwfngnpmiowng3in3gpinmiun3p5iung3ngpi'

CORS(app)
# Register your configurations here (if any)
# app.config.from_object('config.Config')

# Register routes
app.register_blueprint(upload_audio_blueprint, url_prefix='/')
app.register_blueprint(microsoft_auth_blueprint, url_prefix='/')

@app.route('/')
def index():
    # Serve the main page with the audio recording interface
    return render_template('index.html')

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
