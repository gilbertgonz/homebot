from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Shared variable for storing the latest image
shared_frame = None

def gen():
    """Video streaming generator function."""
    vs = cv2.VideoCapture(0)
    while True:
        global shared_frame

        if shared_frame is not None:
            ret, jpeg = cv2.imencode('.jpg', shared_frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        else:
            # If no new image, continue streaming image
            ret, frame = vs.read()
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':   
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
