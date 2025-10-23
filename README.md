<p align="center">

  <h3>🛠️ Technologies Used</h3>
<p align="center">

  <table>
    <tr><td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="50"><br><b>Python</b><br><sub>Core backend language</sub></td></tr>
    <tr><td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" width="55"><br><b>Flask</b><br><sub>Web framework</sub></td></tr>
    <tr><td align="center"><img src="https://raw.githubusercontent.com/napsternxg/spleeter-web/master/static/img/spleeter_logo.png" width="60"><br><b>Spleeter</b><br><sub>AI source separation</sub></td></tr>
    <tr><td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Tailwind_CSS_Logo.svg" width="55"><br><b>Tailwind CSS</b><br><sub>UI Styling</sub></td></tr>
    <tr><td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/3/38/HTML5_Badge.svg" width="50"><br><b>HTML5</b><br><sub>Frontend Structure</sub></td></tr>
    <tr><td align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png" width="50"><br><b>JavaScript</b><br><sub>Frontend Logic</sub></td></tr>
  </table>

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

1. Open `Index.html` in your browser.
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
│   └── Index.html  # Frontend UI
│   ├── style.css           # Tailwind / custom styles
│   └── script.js         # JS for upload & progress
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
