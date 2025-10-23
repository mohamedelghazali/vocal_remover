const uploadStep = document.getElementById('upload-step');
const processingStep = document.getElementById('processing-step');
const downloadStep = document.getElementById('download-step');

const statusMessage = document.getElementById('status-message');
const processingMessage = document.getElementById('processing-message');

const fileUpload = document.getElementById('file-upload');
const fileLabel = document.getElementById('file-label');
const fileName = document.getElementById('file-name');

const processButton = document.getElementById('process-button');

const downloadVocals = document.getElementById('download-vocals');
const downloadInstrumental = document.getElementById('download-instrumental');
const startOverButton = document.getElementById('start-over-button');

const errorBox = document.getElementById('error-box');
const errorMessage = document.getElementById('error-message');

let currentTaskId = null;
let pollInterval = null;

const API_BASE_URL = 'http://127.0.0.1:5000';

fileUpload.addEventListener('change', handleFileSelect);
processButton.addEventListener('click', handleUpload);
startOverButton.addEventListener('click', resetUI);

function handleFileSelect(event) {
    const file = event.target.files[0];
    if (file) {
        if (file.type === 'audio/mpeg' || file.type === 'audio/wav') {
            fileName.textContent = file.name;
            processButton.disabled = false;
            processButton.classList.remove('opacity-50', 'cursor-not-allowed');
            statusMessage.textContent = `Ready to process: ${file.name}`;
            errorBox.classList.add('hidden');
        } else {
            showError('Invalid file type. Please select an MP3 or WAV file.');
            resetUI();
        }
    }
}

async function handleUpload() {
    const file = fileUpload.files[0];
    if (!file) return;

    showProcessingUI('Uploading file...');
    
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(`${API_BASE_URL}/upload`, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || `Server error: ${response.status}`);
        }

        const data = await response.json();
        currentTaskId = data.task_id;
        showProcessingUI('File is in queue. Waiting to process...');
        pollTaskStatus();
        
    } catch (error) {
        console.error('Upload error:', error);
        showError(`Upload failed: ${error.message}. Is the Python server running?`);
    }
}

function pollTaskStatus() {
    if (pollInterval) clearInterval(pollInterval);

    pollInterval = setInterval(async () => {
        if (!currentTaskId) {
            clearInterval(pollInterval);
            return;
        }

        try {
            const response = await fetch(`${API_BASE_URL}/status/${currentTaskId}`);
            
            if (!response.ok) {
                throw new Error(`Server error: ${response.status}`);
            }
            
            const data = await response.json();

            if (data.status === 'SUCCESS') {
                clearInterval(pollInterval);
                showDownloadUI(data.result);
            } else if (data.status === 'FAILURE') {
                clearInterval(pollInterval);
                showError(data.message || 'Processing failed.');
            } else if (data.status === 'PROCESSING') {
                showProcessingUI(data.message || 'Processing...');
            } else {
                showProcessingUI(data.message || 'Waiting in queue...');
            }

        } catch (error) {
            clearInterval(pollInterval);
            console.error('Polling error:', error);
            showError(`Connection lost: ${error.message}. Please check server and try again.`);
        }
    }, 2500);
}

function showProcessingUI(message) {
    uploadStep.classList.add('hidden');
    downloadStep.classList.add('hidden');
    errorBox.classList.add('hidden');
    
    processingStep.classList.remove('hidden');
    processingMessage.textContent = message;
}

function showDownloadUI(result) {
    processingStep.classList.add('hidden');
    uploadStep.classList.add('hidden');
    
    downloadStep.classList.remove('hidden');
    
    downloadVocals.href = `${API_BASE_URL}/download/${currentTaskId}/${result.vocals}`;
    downloadInstrumental.href = `${API_BASE_URL}/download/${currentTaskId}/${result.instrumental}`;
}

function showError(message) {
    processingStep.classList.add('hidden');
    downloadStep.classList.add('hidden');
    
    uploadStep.classList.remove('hidden');
    
    errorBox.classList.remove('hidden');
    errorMessage.textContent = message;
    
    processButton.disabled = true;
    processButton.classList.add('opacity-50', 'cursor-not-allowed');
}

function resetUI() {
    if (pollInterval) clearInterval(pollInterval);
    currentTaskId = null;
    
    downloadStep.classList.add('hidden');
    processingStep.classList.add('hidden');
    errorBox.classList.add('hidden');
    
    uploadStep.classList.remove('hidden');
    
    fileUpload.value = null;
    fileName.textContent = 'Choose an audio file...';
    statusMessage.textContent = 'Upload an audio file (MP3 or WAV) to begin.';
    
    processButton.disabled = true;
    processButton.classList.add('opacity-50', 'cursor-not-allowed');
}
