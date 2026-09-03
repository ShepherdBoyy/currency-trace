# Currency Trace - Backend

Flask API serving a custom-trained TensorFlow Lite object detection model for currency recognition.

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