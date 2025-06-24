import cv2
import numpy as np
from typing import List


def detect_significant_movement(frames: List[np.ndarray], threshold: float = 1.75) -> List[int]:
    """
    Detect frames where significant camera movement occurs.
    Args:
        frames: List of image frames (as numpy arrays).
        threshold: Sensitivity threshold for the magnitude of optical flow.
                   This value may need tuning.
    Returns:
        List of indices where significant movement is detected.
    """
    movement_indices = []

    # Check if there are enough frames to compare
    if len(frames) < 2:
        return []

    # # Convert the first frame to grayscale if the frame is not gray
    frame = frames[0]
    if len(frame.shape) == 3 and frame.shape[2] == 3:
        prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        prev_gray = frame

    for idx, frame in enumerate(frames[1:], 1):  # Start from the second frame
        # Convert current frame to grayscale if the frame is not gray

        if len(frame.shape) == 3 and frame.shape[2] == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            gray = frame

        # Calculate dense optical flow using Farneback's algorithm
        # This returns a 2-channel array with optical flow vectors (dx, dy)
        flow = cv2.calcOpticalFlowFarneback(
            prev=prev_gray,
            next=gray,
            flow=None,
            pyr_scale=0.5,
            levels=3,
            winsize=15,
            iterations=3,
            poly_n=5,
            poly_sigma=1.2,
            flags=0
        )

        # Calculate the magnitude of the flow vectors
        magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

        # Calculate the mean of the magnitude as a movement score
        score = np.mean(magnitude)

        # If the score is above the threshold, record it
        if score > threshold:
            movement_indices.append(idx)

        # Update the previous frame
        prev_gray = gray

    return movement_indices

