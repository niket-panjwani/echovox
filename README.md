# Echovox

Echovox is a voice-activated personal assistant built using Flask, designed to capture user's speech input, convert it to text, and perform various tasks based on commands. It utilizes powerful libraries such as `SpeechRecognition`, `pydub`, and `gTTS` for processing and responding to voice commands.

## Features

- **Voice Command Recognition**: Converts spoken commands to text.
- **Text-to-Speech Response**: Generates spoken feedback to the user.
- **Audio File Conversion**: Handles different audio formats for processing.

## Installation

Before installing Echovox, ensure you have Python 3.6+ and pip installed on your system.

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/yourgithub/echovox.git
   cd echovox
   ```

2. **Create and Activate a Virtual Environment**

- On macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

- On Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. **Install Dependencies**

  ```bash
  pip install -r requirements.txt
  ```

Usage
-----

1.  **Start the Flask Application**
    
    ```bash
    `python run.py`
    ```
    
    This will start the Flask server on `http://127.0.0.1:5000/`.
    
2.  **Interacting with Echovox**
    
    Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with Echovox. You can start recording your voice commands through the web interface.
    

How It Works
------------

*   **Capturing Voice Input**: Uses the Web Audio API in the browser to capture voice commands.
*   **Voice to Text**: Utilizes the `SpeechRecognition` library to convert voice input to text.
*   **Executing Commands**: Based on the recognized text, Echovox performs predefined actions.
*   **Responding to Commands**: Uses `gTTS` for generating voice responses to the user.

File Structure
--------------

Below is the basic file structure of the Echovox project:

```
echovox/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── routes/
│ │ └── web_interface.py
│ ├── assistant/
│ │ ├── init.py
│ │ ├── speech_recognition.py
│ │ └── text_to_speech.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ ├── css/
│ └── js/
├── venv/
├── requirements.txt
└── run.py
```

Contributing
------------

We welcome contributions to Echovox! Please feel free to submit pull requests or open issues to improve the project.

License
-------

Echovox is released under the MIT License. See the LICENSE file for more details.

