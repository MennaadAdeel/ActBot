import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

import cv2
import dlib
import numpy as np
import subprocess
import time

# Constants
CAMERA_IDX = 0
BLINK_THRESHOLD = 0.2  # Adjust as needed
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
MIN_BLINK_DURATION = 0.1  # Minimum duration of a blink in seconds
IMAGE_PATH = "/home/ActBot/Desktop/captured_image.jpg"
PREDICTOR_PATH = "/path/to/shape_predictor_68_face_landmarks.dat"  # Update this path

def capture_image():
    # Capture an image using libcamera-still
    result = subprocess.run(["libcamera-still", "-o", IMAGE_PATH, "--nopreview", "-t", "1000", "--width", str(FRAME_WIDTH), "--height", str(FRAME_HEIGHT)], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error capturing image: {result.stderr}")
        return None

    # Check if the image file exists
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found at {IMAGE_PATH}")
        return None

    # Read the captured image using OpenCV
    image = cv2.imread(IMAGE_PATH)
    if image is None:
        print("Failed to read image using OpenCV")
    return image

def detect_faces(gray_frame, detector):
    return detector(gray_frame)

def calculate_ear(eye_points):
    A = np.linalg.norm(eye_points[1] - eye_points[5])
    B = np.linalg.norm(eye_points[2] - eye_points[4])
    C = np.linalg.norm(eye_points[0] - eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear

def detect_blinks(faces, predictor, gray_frame, blink_threshold=0.2, min_blink_duration=0.1):
    blink_counter = 0
    blink_start_time = None

    for face in faces:
        landmarks = predictor(gray_frame, face)

        # Extract left and right eye coordinates
        left_eye_pts = np.array([(landmarks.part(n).x, landmarks.part(n).y) for n in range(36, 42)], np.int32)
        right_eye_pts = np.array([(landmarks.part(n).x, landmarks.part(n).y) for n in range(42, 48)], np.int32)

        # Calculate EAR for both eyes
        left_ear = calculate_ear(left_eye_pts)
        right_ear = calculate_ear(right_eye_pts)

        # Average the EARs for both eyes for a more stable measurement
        ear = (left_ear + right_ear) / 2.0

        # Detect blink
        if ear < blink_threshold:
            if blink_start_time is None:
                blink_start_time = time.time()
        else:
            if blink_start_time is not None:
                blink_duration = time.time() - blink_start_time
                if blink_duration >= min_blink_duration:
                    blink_counter += 1
                blink_start_time = None

    return blink_counter

def calculate_distraction(frame_counter, blink_counter, is_looking_away_count):
    #percentage_blinks = (blink_counter / frame_counter) * 100
    percentage_looking_away = (frame_counter - is_looking_away_count) / frame_counter * 100
    return percentage_blinks, percentage_looking_away

def main():
    # Load dlib's face detector and facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    blink_counter = 0
    frame_counter = 0
    is_looking_away_count = 0

    while True:
        # Capture an image
        frame = capture_image()
        if frame is None:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(gray, detector)

        if len(faces) == 0:
            is_looking_away_count += 1

        #blink_counter += detect_blinks(faces, predictor, gray, BLINK_THRESHOLD, MIN_BLINK_DURATION)
        frame_counter += 1

        # Display the frame
        cv2.imshow("Captured Image", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Calculate and display the blink statistics
    if frame_counter > 0:
        percentage_blinks, percentage_looking_away = calculate_distraction(frame_counter, blink_counter, is_looking_away_count)
        #print(f"Blinks: {blink_counter}, Total Frames: {frame_counter}")
        #print(f"Percentage of Distraction (Blinks): {percentage_blinks:.2f}%")
        print(f"Percentage of Distraction (Looking Away): {percentage_looking_away:.2f}%")
    else:
        print("No frames captured.")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
