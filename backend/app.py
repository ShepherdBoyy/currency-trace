from flask import Flask, jsonify, request
from flask_cors import CORS
from gcolab_detection_image import tflite_detect_images
from io import BytesIO
import os
import threading

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploaded_image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

PATH_TO_MODEL='custom_model_lite/detect.tflite'   # Path to .tflite model file
PATH_TO_LABELS='custom_model_lite/labelmap.txt'   # Path to labelmap.txt file
min_conf_threshold=0.5

def delete_uploaded_file(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        app.logger.error(f"Error deleting file: {e}")

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    image_file = request.files['image']
    print(image_file)

    if image_file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if image_file:
        filename = image_file.filename
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(image_path)
        image_file.save(image_path)

        detected_objects = tflite_detect_images(PATH_TO_MODEL, UPLOAD_FOLDER, PATH_TO_LABELS, min_conf_threshold)

        def delete_file():
            delete_uploaded_file(image_path)

        # Start a new thread to delete the image file
        threading.Thread(target=delete_file).start()

        return jsonify({'message': 'File uploaded successfully', 'filename': filename, "results": detected_objects})

if __name__ == '__main__':
    app.run(debug=True)