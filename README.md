AI Vocal Remover

A web application that separates vocals from music in any audio file using Python and Spleeter.

This project consists of a Python Flask backend that handles AI processing and a simple HTML/CSS/JavaScript frontend for the user interface.

Features

Vocal & Music Separation: Splits any .mp3 or .wav file into two separate tracks:

vocals.wav (Acapella)

instrumental.wav (Music)

Simple Web Interface: Easy drag-and-drop file uploading.

Asynchronous Processing: Uses threading to process audio in the background without freezing the server.

Real-time Progress: The frontend polls the server to show the user the current processing status.

Direct Downloads: Download the separated audio files directly from the browser.

Tech Stack

Backend:

Python 3

Flask: To create the web server and API endpoints.

Spleeter: The AI model (by Deezer) used for high-quality audio source separation.

Frontend:

HTML5

Tailwind CSS: For modern UI styling.

JavaScript (ES6+): To handle file uploads, API requests (fetch), and status polling.

How to Run

This project is designed to run locally from two files.

1. Backend Setup (Python)

Install Python: Ensure you have Python 3.8 or newer installed.

Install FFmpeg: Spleeter requires FFmpeg. You can download it from ffmpeg.org and add it to your system's PATH.

Install Libraries: Open your terminal and install the required Python packages:

pip install Flask Flask-Cors spleeter ffmpeg-python


Run the Server: In your terminal, navigate to the project directory and run:

python main.py


The server will start on http://127.0.0.1:5000. Leave this terminal running.

2. Frontend Usage

Open the HTML File: In the same project folder, find the vocal_remover.html file.

Double-click vocal_remover.html to open it in your web browser (e.g., Chrome, Firefox).

Use the App:

Select an .mp3 or .wav file.

Click "Separate Audio."

Wait for the processing to finish.

Download your files!

Author & Acknowledgement

Developer: Mohamed El Ghazali

Project: This application was developed as part of an artificial intelligence training course supervised by Mohamed El Ghazali.
