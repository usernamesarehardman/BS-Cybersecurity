const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('file-input');
const browseBtn = document.getElementById('browse-btn');
const uploadBtn = document.getElementById('upload-btn');
const fileNameDisplay = document.getElementById('file-name-display');
const form = document.getElementById('upload-form');

// Prevent default drag behaviors
dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dropArea.classList.add('dragging');
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('dragging');
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dropArea.classList.remove('dragging');
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        updateFileNameDisplay(files[0]);
    }
});

// Open file dialog when clicking the Browse button
browseBtn.addEventListener('click', () => {
    fileInput.click();
});

// Set file input value when files are selected manually
fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        updateFileNameDisplay(fileInput.files[0]);
    }
});

// Update the file name display and enable the upload button
function updateFileNameDisplay(file) {
    fileNameDisplay.textContent = `Selected file: ${file.name}`;
    uploadBtn.disabled = false;
}

// Optional: Add a submit handler if needed to show an upload confirmation
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    fetch('/uploads', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.text())
    .then(message => alert(message))
    .catch(error => console.error('Error:', error));
});