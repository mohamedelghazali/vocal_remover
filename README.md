<p align="center">

  <h3>🛠️ Technologies Used</h3>

  <p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="55" alt="Python Logo">
    <b>Python</b> – Core language for backend development
  </p>

  <p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" width="60" alt="Flask Logo">
    <b>Flask</b> – Lightweight backend web framework
  </p>

  <p>
    <img src="https://raw.githubusercontent.com/napsternxg/spleeter-web/master/static/img/spleeter_logo.png" width="70" alt="Spleeter Logo">
    <b>Spleeter</b> – AI model for vocal & instrumental separation
  </p>

  <p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" width="60" alt="Tailwind Logo">
    <b>Tailwind CSS</b> – Modern frontend styling framework
  </p>

  <p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/HTML5_Badge.svg" width="55" alt="HTML5 Logo">
    <b>HTML5</b> – Structure of the web app
  </p>

  <p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png" width="55" alt="JavaScript Logo">
    <b>JavaScript</b> – Dynamic interactions & client-side logic
  </p>

  <p>
    <img src="https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative&logoColor=white" alt="MIT License">
    <b>License:</b> MIT
  </p>

  <p>
    <img src="https://img.shields.io/badge/Status-Active-success?logo=github" alt="Active Status">
    <b>Status:</b> Active Development
  </p>

</p>




## 🧠 Overview

**AI Vocal Remover** is a modern **web application** that separates vocals from background music in any `.mp3` or `.wav` file using **Python** and **Spleeter**.  
It combines a powerful **Flask backend** for AI-based audio processing with a clean and intuitive **HTML/CSS/JS frontend**.

---

## ✨ Features

- 🎵 **Vocal & Music Separation**  
  Splits any audio file into:
  - `vocals.wav` → (Acapella)  
  - `instrumental.wav` → (Music Only)

- 🖱️ **Simple Web Interface**  
  Drag-and-drop file upload with progress feedback.

- ⚙️ **Asynchronous Processing**  
  Uses background threads for smooth, non-blocking performance.

- 📈 **Real-time Progress Tracking**  
  The frontend continuously polls the backend for current status updates.

- ⬇️ **Instant Download Links**  
  Directly download processed audio files via the browser.

---

## 🧰 Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Backend** | 🐍 Python 3.8+ · 🌐 Flask · 🤖 Spleeter (Deezer) · 🎬 FFmpeg |
| **Frontend** | 🧱 HTML5 · 🎨 Tailwind CSS · ⚡ JavaScript (ES6+) |
| **Deployment** | 💻 Localhost / Custom Server |

---

## ⚙️ Installation & Setup

### 🔹 1. Backend Setup (Python)

#### Step 1 — Install Dependencies
Make sure you have **Python 3.8+** and **FFmpeg** installed.

```bash
pip install Flask Flask-Cors spleeter ffmpeg-python
````

#### Step 2 — Run the Flask Server

```bash
python main.py
```

The backend runs locally at:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

### 🔹 2. Frontend Usage

1. Open `vocal_remover.html` in your browser.
2. Select your `.mp3` or `.wav` file.
3. Click **“Separate Audio”**.
4. Wait for AI processing to complete.
5. Download your `vocals.wav` and `instrumental.wav`.

---

## 🧩 Folder Structure

```
AI-Vocal-Remover/
│
├── main.py                 # Flask backend server
├── 
│   ├── style.css           # Tailwind / custom styles
│   └── script.js           # JS for upload & progress
├── 
│   └── vocal_remover.html  # Frontend UI
├── separated_audio/        # Output folder for vocals & instrumentals
└── README.md
```

---

## 👨‍💻 Author & Acknowledgment

**Developer:** Mohamed El Ghazali
**Project:** Developed as part of an **Artificial Intelligence Training Program** supervised by *Mohamed El Ghazali*.

---

<div align="center">

⭐ *If you find this project helpful, consider giving it a star on GitHub!*
📩 *Contributions, suggestions, and pull requests are always welcome.*

</div>
```
