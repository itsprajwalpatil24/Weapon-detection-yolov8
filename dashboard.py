import streamlit as st
import os
from PIL import Image

# Paths
LOG_FILE = "detections/log.txt"
IMAGE_DIR = "detections"

# Streamlit page settings
st.set_page_config(page_title="Weapon Detection Logs", layout="wide")
st.title("🔍 Weapon Detection Log Dashboard")

# Check if log file exists
if not os.path.isfile(LOG_FILE):
    st.warning("No detection logs found yet.")
else:
    with open(LOG_FILE, "r") as f:
        log_entries = f.readlines()

    if not log_entries:
        st.info("Detection log is currently empty.")
    else:
        st.subheader(f"Total Detections: {len(log_entries)}")
        st.markdown("---")

        # Show logs in reverse (latest first)
        for entry in reversed(log_entries):
            try:
                timestamp, label = entry.strip().split(" - ")
                image_path = os.path.join(IMAGE_DIR, f"{timestamp}.jpg")

                if os.path.exists(image_path):
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(image_path, caption=timestamp, width=150)
                    with col2:
                        st.markdown(f"🕒 **Time Detected:** `{timestamp}`")
                        st.markdown(f"🔫 **Weapon Detected:** `{label}`")
                        st.markdown("---")
                else:
                    st.warning(f"Image not found for timestamp: {timestamp}")

            except Exception as e:
                st.error(f"Error parsing log line: {entry.strip()} — {e}")
