import os

import cv2
from tqdm import tqdm

from .algorithms import (
    background_subtraction,
    histogram_comparison,
    mean_squared_error,
    optical_flow,
    phase_correlation,
    pixelwise,
    sift_matching,
)
from .utils import export_frame, read_video


class Framer:
    def __init__(self) -> None:
        self.algorithms = {
            "pixelwise": pixelwise,
            "background_subtraction": background_subtraction,
            "optical_flow": optical_flow,
            "histogram_comparison": histogram_comparison,
            "sift_matching": sift_matching,
            "mean_squared_error": mean_squared_error,
            "phase_correlation": phase_correlation,
        }

    def process_frames(self, frames, algorithm="pixelwise"):
        if algorithm not in self.algorithms:
            raise ValueError(f"Unsupported algorithm: {algorithm}")

        algorithm_func = self.algorithms[algorithm]

        processed_frames = []
        frame_indices = []
        previous_frame = None
        for i in tqdm(range(len(frames) - 1)):
            current_frame = frames[i]
            if previous_frame is None:
                processed_frames.append(current_frame)
                frame_indices.append(i)
                previous_frame = current_frame
                continue

            significant_change = algorithm_func(previous_frame, current_frame)

            if significant_change:
                processed_frames.append(current_frame)
                frame_indices.append(i)
                previous_frame = current_frame

        print(f"Detected {len(processed_frames)} from {len(frames)} keyframes")

        return processed_frames, frame_indices

    def process_video(
        self, video_path, algorithm="mean_squared_error", output_dir="output/keyframes"
    ):
        frames = read_video(video_path)
        keyframes, frame_indices = self.process_frames(frames, algorithm=algorithm)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for frame, index in tqdm(zip(keyframes, frame_indices)):
            output_path = os.path.join(output_dir, f"keyframe_{index}.jpg")
            export_frame(frame, output_path)

        return keyframes, frame_indices
