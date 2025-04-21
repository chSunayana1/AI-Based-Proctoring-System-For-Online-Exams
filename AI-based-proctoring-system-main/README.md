# 🎥 AI-Powered Proctoring System for Exams  

This project is an **AI-powered proctoring system** that monitors students during online exams using **OpenCV and YOLOv8**. It detects **multiple faces (cheating detection), gaze direction (looking away), and objects (unauthorized items like mobile phones)** in real-time.  

## 🚀 Features
- **Face Detection**: Detects students using OpenCV’s Haar Cascade.
- **Multiple Faces Detection**: Identifies multiple people in the frame (possible cheating).
- **Gaze Tracking**: Alerts if the student looks away.
- **YOLOv8 Object Detection**: Detects unauthorized objects in the exam environment.
- **Real-Time Monitoring**: Continuously processes webcam footage.

## 🎯 How It Works
- Uses OpenCV's Haar Cascade for face detection (avoids dlib dependency).
- Uses YOLOv8 for real-time object detection.
- If multiple faces are detected, an alert is displayed.
- If the student looks away, an alert is shown.

## 🔥 Future Enhancements
- Improve gaze tracking accuracy.
- Add head pose estimation.
- Store violations in a log file.
