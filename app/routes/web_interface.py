from flask import Flask, request, jsonify, Blueprint, send_file
from app.assistant.speech_recognition import recognize_speech_from_file # Assume you have this function
from app.assistant.text_to_speech import text_to_speech
from app.assistant.nlp import MeetingSchedulerClassifier

app = Flask(__name__)

upload_audio_blueprint = Blueprint('upload_audio', __name__)

@upload_audio_blueprint.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Recognize speech from the uploaded file
    recognized_text = recognize_speech_from_file(file)

    # Check if the recognized text is about scheduling a meeting
    classifier = MeetingSchedulerClassifier()
    is_meeting_request = classifier.predict(recognized_text)    

    # Generate audio response from the recognized text
    if is_meeting_request:
        response_text = "Sure, I can help you with that. When would you like to schedule the meeting?"
    else:
        response_text = "I'm sorry, I didn't catch that. Could you please repeat?"
  
    response_audio_path = text_to_speech(response_text)

    # Return the audio file as response
    return send_file(response_audio_path, mimetype="audio/mp3", as_attachment=True, download_name="response.mp3")
