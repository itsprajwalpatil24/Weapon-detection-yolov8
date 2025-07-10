import cv2
import os
from datetime import datetime
from ultralytics import YOLO
from send_email import send_email_alert

# Load the trained YOLOv8 model
model = YOLO(r"C:\Users\PRAJWAL\Desktop\weapon-detection-streamlit\weapon-retrain\run1\weights\best.pt")

# Start webcam capture
cap = cv2.VideoCapture(0)

# Create a folder for detections and a log file
os.makedirs("detections", exist_ok=True)
log_file = "detections/log.txt"

# Flag to prevent duplicate alerts for same detection
alert_sent = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection on current frame
    results = model(frame)

    # Filter predictions with confidence > 0.5
    detected_classes = []
    if results[0].boxes is not None:
        for box in results[0].boxes:
            if box.conf[0] > 0.5:
                detected_classes.append(int(box.cls[0]))

    # Get class labels from the model
    class_names = model.names

    # If any weapon detected in the frame
    if any(cls in range(len(class_names)) for cls in detected_classes):
        if not alert_sent:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            image_path = f"detections/{timestamp}.jpg"

            # Save frame with bounding boxes
            annotated_frame = results[0].plot()
            cv2.imwrite(image_path, annotated_frame)

            # Prepare email content
            labels = ", ".join([class_names[cls] for cls in detected_classes])
            subject = "Weapon Detected!"
            body = f"Weapon(s) Detected: {labels}\nTime: {timestamp}"

            # Send alert email
            send_email_alert(subject, body, attachment_path=image_path)
            print("✅ Email sent!")

            # Log detection
            with open(log_file, "a") as log:
                log.write(f"{timestamp} - {labels}\n")

            alert_sent = True
    else:
        alert_sent = False  # Reset alert flag if no weapon detected

    # Display the live annotated frame
    cv2.imshow("Weapon Detection - Live Feed", results[0].plot())

    # Exit loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
