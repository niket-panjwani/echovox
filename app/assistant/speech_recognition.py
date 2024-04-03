import speech_recognition as sr
from pydub import AudioSegment
import os
from tempfile import NamedTemporaryFile

def recognize_speech_from_file(audio_file):
    # Assuming audio_file is a file object from Flask's request.files['file']

    # Create a temporary file to save the uploaded file for processing
    with NamedTemporaryFile(delete=False) as temp:
        audio_file.save(temp.name)
        temp_file_path = temp.name

    # Now, convert the saved file to the desired format if necessary
    sound = AudioSegment.from_file(temp_file_path, format="webm")
    # Note: Adjust the format as needed based on your actual file format

    # Create another temporary WAV file for processing
    temp_wav_path = temp_file_path + ".wav"
    sound.export(temp_wav_path, format="wav")

    # Now use speech_recognition to process the WAV file
    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = "Could not understand audio"
        except sr.RequestError as e:
            text = f"Could not request results; {e}"

    # Cleanup temporary files
    os.remove(temp_file_path)
    os.remove(temp_wav_path)

    return text
