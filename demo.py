import os
from keyframe.framer import Framer


def main():
    video_path = "asset/short.mp4"
    output_dir = "output"

    # Choose the keyframe detection algorithm
    algorithm = "mean_squared_error"  # You can choose from "pixelwise", "background_subtraction", "optical_flow", etc.

    # Initialize the Framer class
    framer = Framer()

    print(f"Processing video: {video_path} using {algorithm} algorithm")
    keyframes, frame_indices = framer.process_video(
        video_path, algorithm=algorithm, output_dir=output_dir
    )

    # Output the results
    print(f"Detected {len(keyframes)} keyframes.")
    print(f"Keyframes saved to: {os.path.abspath(output_dir)}")


if __name__ == "__main__":
    main()
