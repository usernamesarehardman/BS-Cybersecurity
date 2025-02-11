# CYBS-3913 Term-Project (WIP)

## Due Date: TBD

## Overview
This project implements a simple drag and drop file upload feature using Flask. Users can drag files into a designated area on the webpage, and the files will be uploaded to the server for further processing or storage.

## Objectives
1. Read all configuration files
2. Find all IPv4 addresses in each configuration file
3. Replace it with Class C private IP address
4. Create a log file for each transaction with a time stamp
5. `<Extra>` find a configuration file, which contains MAC address 96:49:18:8A:D6:B9

## Repository Structure
```
📁 websitename.domain/   
├── 📁 static/              # Folder for static files (JS, CSS, etc.)  
│   ├── 📁 css/  
│   │   └── 📄 style.css    # CSS for styling the webpage 
│   ├── 📁 images/  
│   │   └── ...             # Location for future images to be stored
│   └── 📁 js/
│       └── 📄 script.js    # JavaScript for handling file drop and preview
├── 📁 templates/           # Folder containing HTML files
│   ├── 📄 index.html       # Homepage
│   └── ...                 # Future pages will be located here       
├── 📁 uploads              # Folder containing user-uploaded files  
├── 📄 app.py               # Python script containing the Flask application  
└── 📄 README.md            # This file  
```

## Setup Instructions

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.x
- Flask (`pip install flask`)

### Installation
1. See how to clone this repository [here](https://github.com/usernamesarehardman/BS-Cybersecurity/blob/main/README.md)

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

4. Visit `http://127.0.0.1:5000` in your browser to test the file upload functionality.

## Implementation Details

### `app.py`
- Contains the Flask app, which serves the HTML page and handles file uploads.
- Configured to save uploaded files to the `uploads/` directory.
- Checks if the uploaded file is valid, and if not, returns appropriate error messages.

### `index.html`
- The main webpage template where the user interacts with the drag-and-drop file upload area.
- Uses JavaScript to handle the drag-and-drop interaction and display the name of the file before uploading.

### `script.js`
- Handles the drag-and-drop functionality and file previews.
- Ensures smooth user experience by displaying file names and providing feedback if an invalid file type is uploaded.

## Example Output

After uploading a file, you should see a confirmation message like:
```
File uploaded successfully!
```

## References
1. ChatGPT. (2025). *Content partially generated using OpenAI's ChatGPT-4o*. Retrieved from OpenAI API.