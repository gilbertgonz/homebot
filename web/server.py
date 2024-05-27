import cv2
import requests
from datetime import datetime
import os

# Email lib
from libs.notifications import *

# Flask lib
from flask import Flask, render_template, Response, request, jsonify
from flask_basicauth import BasicAuth

# Global vars
ENABLE_NOTIFICATIONS = int(os.environ.get('ENABLE_NOTIFICATIONS'))
ENABLE_DETECTION = int(os.environ.get('ENABLE_DETECTION'))
INIT_VID = False
VS = None

# Detection lib
if ENABLE_DETECTION: # only import if detection enabled so we don't download yolov8n for no reason ;)
    from libs.detect import *

app = Flask(__name__)

## TODO: create seperate thread/process for email notifiations

def gen():
    '''
    Video streaming generator function.
    '''
    global INIT_VID # yes, i know 'global' vars are not cute, its just a prototype
    global VS

    if not INIT_VID: # only initialize once for all clients
        VS = cv2.VideoCapture(0)
        INIT_VID = True

    try:
        while True:
            ret, frame = VS.read()
            
            if not ret:
                break

            detected_human = False
            if ENABLE_DETECTION:
                frame, detected_human = detect(frame)

            # Encode frames
            ret, jpeg = cv2.imencode('.jpg', frame)
            encoded_annotated_frame = jpeg.tobytes()
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_annotated_frame + b'\r\n'
            )

            if detected_human and ENABLE_NOTIFICATIONS:
                sub = f"HomeBot: New human detected"
                msg = ""
                send_email(sub, msg, frame)

    except cv2.error as e:
        # Handle the OpenCV error
        print(f"OpenCV Error: {e}")
    finally:
        VS.release() 
        INIT_VID = False

def return_img():
    '''
    Return a single image from the camera
    '''
    if INIT_VID:
        ret, frame = VS.read()
        if not ret:
            print("Failed to connect to camera")
            return None
        return frame
    else:
        return None
    
@app.route('/ip_notify')
def ip_notify():
    '''
    Logging and showing IP address info
    '''
    ip = request.remote_addr

    # Geolocation API URL
    api_url = f"http://ip-api.com/json/{ip}"

    # Make GET request
    response = requests.get(api_url)

    # Timestamp
    current_time = datetime.now()
    timestamp = current_time.strftime("%d/%b/%Y %H:%M:%S")

    # Create save dir
    dir = '/server_logs'
    if not os.path.exists(dir):
        os.makedirs(dir)
    file_name = f'{dir}/server_log.txt'

    # Default log msg and gps_data
    log_msg = f"{timestamp} --- IP Address: {ip}"
    gps_data = {
        'latitude': "INVALID",
        'longitude': "INVALID"
    }

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            log_msg = f"{timestamp} --- IP Address: {data['query']}, Location: [{data['city']}, {data['regionName']}, {data['country']}], GPS Coord: [{data['lat']}, {data['lon']}]"
            gps_data = {
                'latitude': f"{data['lat']}",
                'longitude': f"{data['lon']}"
            }  

    # Write to txt file
    with open(file_name, 'a') as f:
        f.write(log_msg + '\n')

    # Send notifications if enabled
    if ENABLE_NOTIFICATIONS:
        img = return_img()
        sub = f"HomeBot: New user"
        send_email(sub, log_msg, img=None)
        # send_text(sub, log_msg, img)

    return jsonify(gps_data)

@app.route('/')
def index():
    '''
    Video streaming home page.
    '''
    ip_notify()
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    '''
    Video streaming route
    '''
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Setting up basic authentication
    app.config['BASIC_AUTH_USERNAME'] = str(os.environ.get('USER'))
    app.config['BASIC_AUTH_PASSWORD'] = str(os.environ.get('PASSWD'))
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)

    app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=False, threaded=True)