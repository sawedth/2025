import streamlit as st
import numpy as np
import cv2
from PIL import Image
import movement_detector
import object_movement_detector

st.title("Camera Movement Detection Demo")
st.write(
    "Upload a sequence of images (e.g., from a camera). The app will detect frames with significant camera movement "
    "and object movement."
)

uploaded_files = st.file_uploader(
    "Choose image files", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)

if uploaded_files:
    frames = []
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        frame = np.array(image)
        if frame.shape[-1] == 4:  # RGBA to RGB
            frame = frame[:, :, :3]
        frames.append(frame)

    st.write(f"Loaded {len(frames)} frames.")
    movement_indices = movement_detector.detect_significant_movement(frames)
    object_movement_indices = object_movement_detector.detect_object_movement(frames)
    st.write("Significant movement detected at frames:", movement_indices)

    # Optionally show frames with detected movement
    for idx in movement_indices:
        st.image(frames[idx], caption=f"Movement at frame {idx}", use_container_width=True)

    st.write("Object movement detected at frames:", object_movement_indices)

    for index in object_movement_indices:
        st.image(frames[index], caption=f"Object movement at frame {index}", use_container_width=True)
