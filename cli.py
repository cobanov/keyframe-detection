import argparse
import os
from keyframe.framer import Framer


def main():
    parser = argparse.ArgumentParser(
        description="Keyframe Detection CLI using various algorithms."
    )

    parser.add_argument("video_path", type=str, help="Path to the input video file.")

    parser.add_argument(
        "-a",
        "--algorithm",
        type=str,
        default="mean_squared_error",
        choices=[
            "pixelwise",
            "background_subtraction",
            "optical_flow",
            "histogram_comparison",
            "sift_matching",
            "mean_squared_error",
            "phase_correlation",
        ],
        help="Keyframe detection algorithm to use (default: mean_squared_error).",
    )

    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default="keyframes_output",
        help="Directory to save the detected keyframes (default: keyframes_output).",
    )

    args = parser.parse_args()
    framer = Framer()

    print(f"Processing video: {args.video_path} using {args.algorithm} algorithm")
    keyframes, frame_indices = framer.process_video(
        args.video_path, algorithm=args.algorithm, output_dir=args.output_dir
    )

    print(f"Detected {len(keyframes)} keyframes.")
    print(f"Keyframes saved to: {os.path.abspath(args.output_dir)}")


if __name__ == "__main__":
    main()
