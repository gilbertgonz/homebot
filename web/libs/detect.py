import cv2
from ultralytics import YOLO
import torch

'''
Notes:
- Installed all major cuda packages on jetson using "sudo apt install nvidia-jetpack"
- Fixed "torch with no cuda" issue by installing cuda locally (https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)
- Fixed "libcudnn9.so file not found" error by installing it `sudo apt-get install libcudnn9 libcudnn9-dev`
'''

track_ids = []
def detect(cv_image):
    detection = False
    results = model.track(cv_image, classes=0, conf=0.5, verbose=False, persist=True) # only detect humans

    if results[0].boxes is not None and results[0].boxes.id is not None:
        annotated_frame = results[0].plot()
        boxes = results[0].boxes.xywh.cpu()
        track_id = results[0].boxes.id.int().cpu().tolist()

        if track_id not in track_ids:
            detection = True
            track_ids.append(track_id)

        return annotated_frame, detection
    else:
        return cv_image, detection

    

# Load YOLO model
model = YOLO("yolov8n.pt")

# Set GPU if available
if torch.cuda.is_available():
    device = torch.device("cuda") 
else:
    device = torch.device("cpu") 

model.to(device=device)

def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        annotated_frame, _ = detect(frame, model)

        cv2.imshow('Frame', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()