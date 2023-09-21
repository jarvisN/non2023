import cv2
import os

def capture_frames(video_path, output_folder, interval_in_seconds):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        return

    # Get the video's FPS (frames per second)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Calculate the frame interval based on the desired interval in seconds
    frame_interval = int(interval_in_seconds * fps)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # If this frame is an interval frame, save it
        if frame_count % frame_interval == 0:
            save_path = os.path.join(output_folder, f"frame_{saved_count}.jpg")
            cv2.imwrite(save_path, frame)
            saved_count += 1

        frame_count += 1

    # Release the video capture object
    cap.release()

# Example usage
video_path = 'vdo4.mp4'
output_folder = 'image'
interval_in_seconds = 5  # Capture a frame every 5 seconds
capture_frames(video_path, output_folder, interval_in_seconds)
