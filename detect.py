import cv2
from ultralytics import YOLO
import torch

'''
Notes:
- Installed all major cuda packages on jetson using "sudo apt install nvidia-jetpack"
- Fixed "torch with no cuda" issue by installing cuda locally (https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)
- Fixed "libcudnn9.so file not found" error by installing it `sudo apt-get install libcudnn9 libcudnn9-dev`
'''

def detect(cv_image, model, thresh=0.5):
    results = model.predict(cv_image, conf=thresh, verbose=False) # only detect humans

    annotated_frame = results[0].plot()

    for r in results:
        boxes = r.boxes
        for box in boxes:
            bbox = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            x1, y1, x2, y2 = map(int, bbox)
            c = box.cls

    return annotated_frame

def main():
    # Load YOLO model
    model = YOLO("yolov8n.pt")

    # Set GPU if available
    if torch.cuda.is_available():
        device = torch.device("cuda") 
        print("cuda")
    else:
        device = torch.device("cpu") 
        print("cpu")

    model.to(device=device)

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        annotated_frame = detect(frame, model)

        cv2.imshow('Frame', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()