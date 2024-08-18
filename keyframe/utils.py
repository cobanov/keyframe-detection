import cv2


def read_video(video_path):
    """Read a video from the specified path and return a list of frames."""
    print(f"Reading video from: {video_path}")
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames


def export_frame(frame, output_path):
    """Export a single frame to the specified output path."""
    cv2.imwrite(output_path, frame)
