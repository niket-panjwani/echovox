from flask import Flask, render_template
from app.routes.web_interface import upload_audio_blueprint

# Initialize the Flask application
app = Flask(__name__)

# Register your configurations here (if any)
# app.config.from_object('config.Config')

# Register routes
app.register_blueprint(upload_audio_blueprint, url_prefix='/')

@app.route('/')
def index():
    # Serve the main page with the audio recording interface
    return render_template('index.html')

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
