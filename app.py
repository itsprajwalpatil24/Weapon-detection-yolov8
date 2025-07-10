import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

# Page configuration
st.set_page_config(page_title="Weapon Detector", layout="centered")
st.title("🔫 Real-Time Weapon Detection")
st.caption("Upload an image to detect weapons using a custom YOLOv8 model")

# File uploader
uploaded_file = st.file_uploader("📁 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert to numpy array for YOLO input
    img_array = np.array(image)

    # Load YOLOv8 custom model
    model = YOLO("weapon-retrain/run1/weights/best.pt")  # ✅ Update if path changes

    # Run inference
    with st.spinner("Detecting weapons..."):
        results = model(img_array)
        annotated_img = results[0].plot()

    # Display results
    st.success("Detection complete!")
    st.image(annotated_img, caption="Detected Objects", use_container_width=True)
