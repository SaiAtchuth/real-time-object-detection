import time
from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (160, 120))

    if not ret:
        break

    start = time.time()

    results = model(frame)

    end = time.time()

    latency = (end - start) * 1000
    fps = 1 / (end - start)

    annotated = results[0].plot()

    cv2.putText(annotated, f"FPS: {int(fps)}", (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(annotated, f"Latency: {int(latency)} ms", (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()