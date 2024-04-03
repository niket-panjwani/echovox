from gtts import gTTS
import os
from tempfile import NamedTemporaryFile

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    temp_file = NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(temp_file.name)
    return temp_file.name