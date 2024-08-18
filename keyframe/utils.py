import cv2


def read_video(video_path):
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
    """Export a frame to the specified path."""
    cv2.imwrite(output_path, frame)
