import os

from keyframe.framer import Framer


def main():
    framer = Framer()

    video_path = "asset/short.mp4"
    algorithm = "pixelwise"  # [pixelwise, background_subtraction, optical_flow, histogram_comparison, sift_matching, mean_squared_error, phase_correlation]
    output_dir = f"output/{algorithm}_keyframes"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Processing video with '{algorithm}' algorithm...")
    framer.process_video(video_path, algorithm, output_dir)


if __name__ == "__main__":
    main()
