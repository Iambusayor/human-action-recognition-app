# Imports
from flask.globals import current_app
from flask.helpers import send_file, send_from_directory, url_for
from app import app
from flask import render_template, request, redirect
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from app.detector import video_detection

# App configurations
app.config['UPLOAD_PATH'] = str(
    Path(__file__).resolve().parent / 'static/uploads/')
app.config['DOWNLOAD_PATH'] = str(
    Path(__file__).resolve().parent / 'static/detections/')
app.config['ALLOWED_VIDEO_EXTENSIONS'] = ['MP4', 'MOV', 'AVI', 'MKV']



# Home route
@app.route('/')
def index():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Function to confirm the extension of the  uploaded file
def check_extension(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit('.', 1)[1]

    if ext.upper() in app.config['ALLOWED_VIDEO_EXTENSIONS']:
        return True
    else:
        return False

# Upload route
@app.route('/upload-video', methods=['GET', 'POST'])
def upload_video():
    if request.method == "POST":

        if request.files:

            video = request.files['video']

            if video.filename == "":
                return redirect(request.url)

            if not check_extension(video.filename):
                return redirect(request.url)

            else:
                filename = secure_filename(video.filename)
            
            #Where upload will be saved 
            save_path = os.path.join(app.config['UPLOAD_PATH'], filename)
            if not os.path.exists(save_path):
                video.save(save_path)

            # Human activity recognition function function
            video_detection(save_path, filename)
            # redirect to donwload page
            return redirect('/download/'+filename)

    return render_template('upload_video.html')

# route to download video
@app.route('/download/<filename>', methods=['GET', 'POST'])
def download_video(filename):
    print(current_app.root_path)
    return send_from_directory(app.config['DOWNLOAD_PATH'], filename, as_attachment=True)
