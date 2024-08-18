# Keyframe Detection Package

`keyframe` is a Python package designed for detecting keyframes in videos using various algorithms. This package provides an easy-to-use interface for processing video frames and extracting significant frames (keyframes) based on different detection methods.

### Available Algorithms

- **pixelwise**: Compares pixels between frames.
- **background_subtraction**: Uses background subtraction to detect significant changes.
- **optical_flow**: Measures the movement between frames using optical flow.
- **histogram_comparison**: Compares histograms of frames.
- **sift_matching**: Uses SIFT features to detect significant changes.
- **mean_squared_error**: Computes the mean squared error between frames.
- **phase_correlation**: Uses phase correlation to detect keyframes.

## Installation

To install the package, use pip:

```bash
pip install keyframe
```

## Usage

```python
import os
from keyframe.framer import Framer

framer = Framer()

video_path = "asset/short.mp4"
algorithm = "pixelwise"  # [pixelwise, background_subtraction, optical_flow, histogram_comparison, sift_matching, mean_squared_error, phase_correlation]
output_dir = f"output/{algorithm}_keyframes"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Processing video with '{algorithm}' algorithm...")
framer.process_video(video_path, algorithm, output_dir)
```

### Command-Line Interface (CLI)

You can use the CLI to detect keyframes in a video. The detected keyframes will be saved to a specified directory.

```bash
python cli.py path/to/video.mp4 --algorithm pixelwise --output-dir keyframes_output
```

- **`video_path`**: Path to the video file.
- **`--algorithm`**: The algorithm to use for keyframe detection (default: `mean_squared_error`).
- **`--output-dir`**: Directory to save the detected keyframes (default: `keyframes`).

### Example

```bash
python cli.py example_video.mp4 --algorithm optical_flow --output-dir keyframes_output
```

This command processes `example_video.mp4` using the `optical_flow` algorithm and saves the keyframes in the `keyframes_output` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
