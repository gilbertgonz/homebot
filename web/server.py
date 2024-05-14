from flask import Flask, render_template, Response, request, jsonify
from flask_basicauth import BasicAuth
import cv2
import requests
from datetime import datetime
import os

from libs.control import receive

app = Flask(__name__)

# Setting up basic authentication
app.config['BASIC_AUTH_USERNAME'] = str(os.environ.get('USER'))
app.config['BASIC_AUTH_PASSWORD'] = str(os.environ.get('PASSWD'))
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

# Global vars
init_vid = False
vs = None
file_time = None

def gen():
    '''
    Video streaming generator function.
    '''
    global init_vid # yes, i know 'global' vars are not cute, its just a prototype
    global vs

    if not init_vid: # only initialize once for all clients
        vs = cv2.VideoCapture(0)
        init_vid = True

    try:
        while True:
            ret, frame = vs.read()
            
            if not ret:
                break

            # Encode frames
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )
    except cv2.error as e:
        # Handle the OpenCV error
        print(f"OpenCV Error: {e}")
    finally:
        vs.release() 
        init_vid = False

def log_txt(ip):
    global file_time

    # Geolocation API URL
    api_url = f"http://ip-api.com/json/{ip}"

    # Make GET request
    response = requests.get(api_url)

    # Timestamp
    current_time = datetime.now()
    timestamp = current_time.strftime("%d/%b/%Y %H:%M:%S")
    if file_time is None:
        file_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Create save dir
    dir = './server_logs'
    if not os.path.exists(dir):
        os.makedirs(dir)
    file_name = f'{dir}/{file_time}_server_log.txt'


    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'fail': # handling local testing
            log_msg = f"{timestamp} --- IP Address: {ip}"
        else:
            log_msg = f"{timestamp} --- IP Address: {data['query']}, Country: {data['country']}, State: {data['regionName']}, City: {data['city']}, Latitude: {data['lat']}, Longitude: {data['lon']}"
    else:
        log_msg = f"{timestamp} --- IP Address: {ip}"

    # Write to txt file
    with open(file_name, 'a') as f:
        f.write(log_msg + '\n')


@app.route('/')
def index():
    '''
    Video streaming home page.
    '''
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    '''
    Video streaming route
    '''

    log_txt(request.remote_addr)
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/update_joystick', methods=['POST'])
def receive_joystick():
    '''
    Receive data from frontend joystick
    '''
    data = request.json
    receive(data)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True, threaded=True)
