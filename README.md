# AI-Based-Proctoring-System-For-Online-Exams

This project is an AI-driven proctoring solution designed to monitor and flag suspicious behaviors during online exams. It uses computer vision techniques to detect face presence, multiple persons, mobile phone usage, and gaze direction to ensure exam integrity.

---

## 🔍 Features

- ✅ **Face Detection**: Detects and tracks face presence during the exam.
- 👥 **Multiple Face Detection**: Flags if more than one person is detected in the frame.
- 📵 **Mobile Detection**: Alerts if a mobile phone is detected using object detection.
- 👀 **Gaze Detection**: Identifies off-center gaze (left/right) indicating distraction or possible cheating.
- 📹 **Video Recording**: Entire exam session is recorded and saved.
- 📝 **Violation Logging**: Timestamped logs for every detected violation (e.g., multiple faces, mobile usage, off-gaze).
- 🧠 **YOLOv8 Integration**: Efficient object detection via the ultralytics YOLOv8 model.
- 🧑‍💻 **User-Friendly GUI**: Start and stop monitoring using simple buttons.

---

## 🛠️ Technologies Used

- `Python 3.9`
- `OpenCV`
- `Ultralytics YOLOv8`
- `GazeTracking`
- `Tkinter` (for GUI)
- `NumPy`
- `Datetime` (for timestamps)

---

## 📦 Installation

1. **Clone the repository**

```bash
https://github.com/chSunayana1/AI-Based-Proctoring-System-For-Online-Exams.git
cd AI-based-proctoring-system

2. **Install dependencies**

```bash
pip install -r requirements.txt

3.**How to Run**

```bash
python proctoring.py

Click Quit to end the session.

A video will be saved in the root folder.

Violations are logged in separate .txt files.
