from flask import Flask, render_template, Response, request, jsonify
import cv2
from libs.control import receive

app = Flask(__name__)

def gen():
    '''
    Video streaming generator function.
    '''
    vs = cv2.VideoCapture(0)
    
    while True:
        ret, frame = vs.read()
        
        try:
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )
        except cv2.error as e:
            # Handle the OpenCV error
            print(f"OpenCV Error: {e}")
            break

@app.route('/')
def index():
    '''
    Video streaming home page.
    '''
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    '''
    Video streaming route. Put this in the src attribute of img tag.
    '''
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
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
