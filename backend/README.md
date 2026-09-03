<div align="center">

# Currency Trace - Backend

Flask API serving a custom-trained TensorFlow Lite object detection model for currency recognition.

</div>

## Tech Stack

| Technology                   | Purpose                                      |
| ---------------------------- | -------------------------------------------- |
| Python                       | Runtime language                             |
| Flask                        | Web framework / REST API                     |
| Flask-CORS                   | Cross-origin request handling                |
| TensorFlow / TensorFlow Lite | Object detection model inference             |
| OpenCV (opencv-python)       | Image processing                             |
| NumPy                        | Numerical operations for image/model data    |
| Matplotlib                   | Visualization during detection processing    |
| Gunicorn                     | Production WSGI server (used for deployment) |

## Installation

1. Navigate into the backend directory

```bash
    cd backend
```

2. Create and activate a virtual environment

On macOS/Linux:

```bash
    python3 -m venv venv
    source venv/bin/active
```

On Windows:

```bash
    python -m venv venv
    venv\Scripts\activate
```

3. Install dependencies

```bash
    pip install -r requirements.txt
```

4. Run the Flask server

```bash
    python app.py
```

5. The API will be running at `http://localhost:5000`

## Project Structure

```
backend/
├── custom_model_lite/
│   ├── detect.tflite
│   ├── labelmap.txt
│   ├── labelmap.pbtxt
│   ├── pipeline_file.config
│   └── saved_model/
├── currency/
├── uploaded_image/
├── app.py
├── gcolab_detection_image.py
└── requirements.txt
```

## API Overview

### Currency Detection

**POST** `/upload`

Accepts an image file and returns detected currency objects with confidence scores.

**Request:** `multipart/form-data`

| Field   | Type | Description                             |
| ------- | ---- | --------------------------------------- |
| `image` | File | Image of a coin or banknote to identify |

**Response:**

```json
{
  "message": "File uploaded successfully",
  "filename": "example.jpg",
  "results": [
    {
      "label": "20peso",
      "confidence": 0.87
    }
  ]
}
```

**Error response** (no image provided):

```json
{
  "error": "No image uploaded"
}
```