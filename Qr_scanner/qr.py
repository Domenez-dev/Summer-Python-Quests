from flask import Flask, render_template, request, Response, jsonify
import qrcode
import json
import os
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image
import base64
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0)
is_camera_active = False
captured_data = None

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate QR code
@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['data']
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return render_template('index.html', img_str=img_str)

# Route to scan QR code from file
@app.route('/scan', methods=['POST'])
def scan_qr():
    file = request.files['qrfile']
    img = Image.open(file.stream)
    decoded_objects = decode(img)
    decoded_data = [obj.data.decode('utf-8') for obj in decoded_objects]
    return render_template('index.html', decoded_data=decoded_data)

def gen_frames():
    global is_camera_active, captured_data
    while is_camera_active:
        success, frame = camera.read()
        if not success:
            break
        else:
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                points = obj.polygon
                if len(points) > 4:
                    hull = cv2.convexHull(points)
                    points = hull
                n = len(points)
                for j in range(0, n):
                    cv2.line(frame, points[j], points[(j + 1) % n], (0, 255, 0), 3)

                x = obj.rect.left
                y = obj.rect.top
                barcode_data = obj.data.decode('utf-8')
                barcode_type = obj.type
                text = f"{barcode_data} ({barcode_type})"
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                captured_data = barcode_data  # Capture the QR code data
                is_camera_active = False  # Deactivate camera after capturing QR code
                break

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global is_camera_active, captured_data
    is_camera_active = True
    captured_data = None
    return jsonify(status="Camera started")

@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    global is_camera_active
    is_camera_active = False
    return jsonify(status="Camera stopped")

@app.route('/get_captured_data', methods=['GET'])
def get_captured_data():
    global captured_data
    if captured_data:
        return jsonify(data=captured_data)
    else:
        return jsonify(data=None)

if __name__ == '__main__':
    app.run(debug=True)
