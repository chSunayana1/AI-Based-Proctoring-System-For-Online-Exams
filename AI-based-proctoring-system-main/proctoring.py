import cv2
import numpy as np
from ultralytics import YOLO
import datetime
import tkinter as tk
import threading

# Load models
model = YOLO("yolov8n.pt")  
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Flags to control execution
stop_proctoring = False

# One-time alert flags
alert_multiple_faces = False
alert_gaze_away = False
alert_mobile_detected = False

# Time-based filenames
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(f'recorded_exam_{timestamp}.avi', fourcc, 20.0, (640, 480))
log_file = open(f'violation_log_{timestamp}.txt', 'w')

def log_violation(msg):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    log_file.write(f"[{now}] {msg}\n")

def start_proctoring():
    global stop_proctoring
    global alert_multiple_faces, alert_gaze_away, alert_mobile_detected

    cap = cv2.VideoCapture(0)

    while cap.isOpened() and not stop_proctoring:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50, 50))

        if len(faces) > 1:
            cv2.putText(frame, "Multiple Faces Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if not alert_multiple_faces:
                log_violation("ALERT: Multiple faces detected")
                alert_multiple_faces = True

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            nose_x = x + w // 2
            if nose_x < x + 20 or nose_x > (x + w) - 20:
                cv2.putText(frame, "Looking Away!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if not alert_gaze_away:
                    log_violation("ALERT: Gaze deviated / Looking away")
                    alert_gaze_away = True

        # YOLO object detection
        results = model(frame)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls[0])]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
                # Alert once if mobile phone detected
                if label.lower() in ['cell phone', 'mobile phone', 'phone'] and not alert_mobile_detected:
                    log_violation("ALERT: Unauthorized object detected (mobile)")
                    alert_mobile_detected = True

        cv2.putText(frame, "Use GUI to Quit", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

        cv2.imshow("AI Proctoring System", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    log_file.close()
    cv2.destroyAllWindows()
    root.quit()

def quit_proctoring():
    global stop_proctoring
    stop_proctoring = True

# GUI setup
root = tk.Tk()
root.title("Proctoring Controller")
root.geometry("250x100")
tk.Label(root, text="AI Proctoring System", font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Quit Proctoring", command=quit_proctoring, bg="red", fg="white").pack(pady=10)

# Start thread
threading.Thread(target=start_proctoring).start()
root.mainloop()
