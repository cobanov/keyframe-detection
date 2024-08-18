import argparse
from keyframe.framer import Framer


def run_keyframe_detection(video_path, algorithm, output_dir):
    framer = Framer()
    keyframes, indices = framer.process_video(
        video_path, algorithm=algorithm, output_dir=output_dir
    )
    print(f"Detected {len(keyframes)} keyframes. Frames saved to {output_dir}.")


def main():
    parser = argparse.ArgumentParser(description="Keyframe Detection CLI")
    parser.add_argument("video_path", type=str, help="Path to the video file")
    parser.add_argument(
        "--algorithm",
        type=str,
        default="mean_squared_error",
        help="Algorithm to use for detection",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="keyframes",
        help="Directory to save keyframes",
    )

    args = parser.parse_args()

    run_keyframe_detection(args.video_path, args.algorithm, args.output_dir)


if __name__ == "__main__":
    main()
