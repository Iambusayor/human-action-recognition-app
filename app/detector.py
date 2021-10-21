# Import librabries
import os
from pathlib import Path
from deepstack_sdk import ServerConfig, Detection


# Configure deepstack api
config = ServerConfig('http://localhost:80')
detection = Detection(config, name='actionnetv2')


def video_detection(file_path, filename):
    """
        file_path: Where the file is saved in server
        filename: name of file
    """
    # path to save the annotated video
    save_path = os.path.join(
        str(Path(__file__).resolve().parent / 'static/detections/'), filename)
    # deepstack api on video
    detection.detectObjectVideo(file_path, output=save_path)
