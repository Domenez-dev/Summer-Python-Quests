# QR Code Generator and Scanner

This Flask application allows users to generate QR codes and scan them either by uploading an image or using a camera. The application is styled with a blue theme for a polished look and enhanced user experience.

## Features

- **Generate QR Code:** Enter data to generate a QR code.
- **Scan QR Code from Image:** Upload an image file to scan and decode the QR code.
- **Scan QR Code with Camera:** Use your device's camera to scan and decode a QR code in real-time.
- **Styled Interface:** A clean and modern blue-themed interface for a better user experience.

## Requirements

- Python 3.x
- Flask
- Pillow
- pyzbar
- opencv-python
- colorama
- requests
- gunicorn (for production deployment)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/qr-code-generator-scanner.git
    cd qr-code-generator-scanner
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000` to use the application.

## Usage

### Generate QR Code

1. Go to the "Generate QR Code" section.
2. Enter the data you want to encode into the QR code.
3. Click the "Generate" button to create the QR code.
4. The generated QR code will be displayed below the form.

### Scan QR Code from Image

1. Go to the "Scan QR Code" section.
2. Click the "Choose File" button and select an image file containing a QR code.
3. Click the "Scan" button to decode the QR code.
4. The decoded data will be displayed below the form.

### Scan QR Code with Camera

1. Go to the "Scan QR Code with Camera" section.
2. Click the "Start Camera" button to activate your device's camera.
3. Point the camera at the QR code.
4. The scanned QR code data will be displayed below the camera feed.

