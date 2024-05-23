import cv2
from ultralytics import YOLO
import torch

def detect(cv_image, model, thresh=0.5):
    results = model.predict(cv_image, conf=thresh, verbose=False) # only detect humans

    for r in results:
        boxes = r.boxes
        for box in boxes:
            bbox = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
            x1, y1, x2, y2 = map(int, bbox)
            c = box.cls

            # Draw bounding box
            cv2.rectangle(cv_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

def main():
    # Load YOLO model
    model = YOLO("yolov8n.pt")

    # Set GPU if available
    device = torch.device("cuda") 
    # if torch.cuda.is_available():
    #     device = torch.device("cuda") 
    #     print("cuda")
    # else:
    #     device = torch.device("cpu") 
    #     print("cpu")

    model.to(device=device)

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detect(frame, model)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()