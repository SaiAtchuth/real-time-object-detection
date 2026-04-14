# 🚀 Real-Time Object Detection with YOLOv8
![Detection Output](output.png)
## 📌 Overview
This project implements real-time object detection using YOLOv8 and OpenCV. It also measures system performance using FPS (Frames Per Second) and Latency.

---

## ⚙️ Features
- Real-time webcam object detection
- FPS (Frames Per Second) calculation
- Latency measurement (ms)
- Model comparison (YOLOv8n vs YOLOv8s)
- Performance optimization using image resizing

---

## 🧠 Technologies Used
- Python
- OpenCV
- Ultralytics YOLOv8

---

## 📊 Results

| Model     | FPS  | Latency |
|----------|------|--------|
| YOLOv8n  | ~16  | ~60 ms |
| YOLOv8s  | ~8   | ~110 ms |

---

## 🔍 Key Learnings
- Tradeoff between speed and accuracy
- CPU bottleneck in deep learning inference
- Impact of input resolution on performance
- Real-time system design

---

## ▶️ How to Run

```bash
pip install ultralytics opencv-python
python camera_test.py