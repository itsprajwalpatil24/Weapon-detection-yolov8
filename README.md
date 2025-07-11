Real-Time Weapon Detection for Surveillance using YOLOv8

This project detects weapons (knife, pistol, rifle, etc.) in real-time from a live webcam feed using YOLOv8 and OpenCV. On detection, it captures the frame with bounding boxes, sends an email alert with the annotated image, and logs the event with a timestamp.

📌 Current Features:
Real-time detection via webcam
Sends email alerts with detected weapon images
Saves annotated frames with bounding boxes
Maintains detection logs with timestamps

🚀 Future Scope:
Integration with IP/CCTV cameras
Dashboard for multi-camera monitoring
Deployment on edge devices like Raspberry Pi
SMS/Push notifications integration

🔒 Use Case: Security monitoring, restricted area surveillance, border security, home safety systems.

###📦 Download the Trained Model : 
[best.pt] from this link ( https://drive.google.com/file/d/1okvdIzTY2jUBECX9L-C7ZKMqIJkVud_t/view?usp=sharing )
and place it inside.

-----------------------------------------------------------------------------------------------------------------------------

🔸app.py : streamlit based dashboard for Weapon Detection by uploading the image 
🔸dashboard.py :  streamlit based log viewer with detected images(from Real time Webcam) with their timestamps
🔸webcam_detect.py : for detecting weapons using the webcam (Custom Trained YoloV8 Model)
🔸train.py : for training the model 
🔸send_email : for sending email when webcam detects a weapon 


