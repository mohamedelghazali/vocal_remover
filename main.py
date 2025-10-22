import os
import uuid
import threading
import shutil
from multiprocessing import freeze_support
from flask import Flask, request, jsonify, send_from_directory, make_response
from flask_cors import CORS
from spleeter.separator import Separator
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'wav', 'mp3'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)

tasks_status = {}

separator = None
print("Spleeter model will be loaded on startup...")

def run_spleeter_task(task_id, input_path, output_dir_for_task):
    if separator is None:
        tasks_status[task_id] = {'status': 'FAILURE', 'message': 'Spleeter model not loaded.'}
        return

    try:
        print(f"[Task {task_id}] Starting separation for: {input_path}")
        tasks_status[task_id] = {'status': 'PROCESSING', 'message': 'Separating audio...'}

        separator.separate_to_file(input_path, output_dir_for_task)
        
        input_filename_base = os.path.basename(input_path).rsplit('.', 1)[0]
        result_folder = os.path.join(output_dir_for_task, input_filename_base)

        vocals_path = os.path.join(result_folder, 'vocals.wav')
        instrumental_path = os.path.join(result_folder, 'accompaniment.wav')

        if os.path.exists(vocals_path) and os.path.exists(instrumental_path):
            final_vocals_path = os.path.join(output_dir_for_task, 'vocals.wav')
            final_instrumental_path = os.path.join(output_dir_for_task, 'accompaniment.wav')
            
            shutil.move(vocals_path, final_vocals_path)
            shutil.move(instrumental_path, final_instrumental_path)
            
            shutil.rmtree(result_folder)
            os.remove(input_path)

            print(f"[Task {task_id}] Separation complete.")
            tasks_status[task_id] = {
                'status': 'SUCCESS',
                'message': 'Processing complete!',
                'result': {
                    'vocals': 'vocals.wav',
                    'instrumental': 'accompaniment.wav'
                }
            }
        else:
            raise Exception("Spleeter did not produce output files.")
            
    except Exception as e:
        print(f"[Task {task_id}] Error during separation: {e}")
        tasks_status[task_id] = {'status': 'FAILURE', 'message': str(e)}
        if os.path.exists(input_path):
            os.remove(input_path)
        if os.path.exists(output_dir_for_task):
            shutil.rmtree(output_dir_for_task)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file_route():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        task_id = str(uuid.uuid4())
        
        ext = file.filename.rsplit('.', 1)[1].lower()
        
        input_filename = f"{task_id}.{ext}"
        input_path = os.path.join(UPLOAD_FOLDER, input_filename)
        
        output_dir_for_task = os.path.join(OUTPUT_FOLDER, task_id)
        os.makedirs(output_dir_for_task, exist_ok=True)
        
        file.save(input_path)
        
        tasks_status[task_id] = {'status': 'PENDING', 'message': 'Task is queued...'}
        
        thread = threading.Thread(
            target=run_spleeter_task,
            args=(task_id, input_path, output_dir_for_task)
        )
        thread.start()
        
        return jsonify({'task_id': task_id}), 202
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@app.route('/status/<task_id>', methods=['GET'])
def task_status_route(task_id):
    status = tasks_status.get(task_id)
    if not status:
        return jsonify({'status': 'FAILURE', 'message': 'Task not found.'}), 404
    
    return jsonify(status)

@app.route('/download/<task_id>/<filename>', methods=['GET'])
def download_file_route(task_id, filename):
    if filename not in ('vocals.wav', 'accompaniment.wav'):
        return jsonify({'error': 'Invalid file name'}), 400
        
    directory = os.path.join(OUTPUT_FOLDER, task_id)
    
    try:
        return send_from_directory(directory, filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'File not found. It may have expired or failed processing.'}), 404

if __name__ == '__main__':
    freeze_support()

    print("Loading Spleeter model (2stems)...")
    print("This may take a moment on first run as it downloads the model.")
    try:
        separator = Separator('spleeter:2stems-16kHz')
        print("Spleeter model loaded successfully.")
    except Exception as e:
        print(f"Error loading Spleeter model: {e}")
        print("Please ensure you have a working internet connection and ffmpeg is installed.")

    print("-------------------------------------------------")
    print("AI Vocal Remover Server")
    print("Flask server starting on http://127.0.D.1:5000")
    print("Open 'vocal_remover.html' in your browser to use.")
    print("-------------------------------------------------")
    app.run(debug=True, port=5000)

