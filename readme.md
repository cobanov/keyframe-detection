# Framer

Framer is a Python library for detecting keyframes in video sequences using various algorithms. It supports multiple methods for comparing frames and extracting keyframes, making it versatile for different use cases such as video summarization, scene change detection, and more.

## Features

- **Multiple Algorithms**: Choose from a variety of algorithms including pixel-wise difference, structural similarity, optical flow, histogram comparison, feature matching, and more.
- **Video Processing**: Load and process video files to extract keyframes.
- **Export Keyframes**: Save detected keyframes as images.

## Installation

You can install Framer using pip:

```bash
pip install framer
```

Alternatively, you can clone the repository and install the dependencies using:

```bash
git clone https://github.com/yourusername/framer.git
cd framer
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
import cv2
from framer import Framer

# Initialize Framer
framer = Framer()

# Load and process a video to detect keyframes using the 'structural_similarity' algorithm
keyframes = framer.process_video("video.mp4", algorithm="structural_similarity", output_dir="keyframes")

print(f"Detected {len(keyframes)} keyframes.")
```

### Available Algorithms

Framer supports several algorithms for keyframe detection:

- `pixelwise`: Pixel-wise absolute difference.
- `background_subtraction`: Background subtraction using MOG2.
- `optical_flow`: Optical flow (supports Lucas-Kanade and Farneback methods).
- `structural_similarity`: Structural Similarity Index (SSIM).
- `histogram_comparison`: Histogram comparison.
- `feature_matching`: Feature matching using ORB.
- `sift_matching`: Feature matching using SIFT.
- `mean_squared_error`: Mean Squared Error.
- `block_matching`: Block matching (placeholder, update as needed).
- `phase_correlation`: Phase correlation.

### Exporting Keyframes

Keyframes can be exported to a specified directory using the `export_frame()` method:

```python
# Export a single frame
framer.export_frame(keyframes[0], "output/keyframe_0.jpg")
```

### Processing Video Files

To process an entire video and extract keyframes:

```python
keyframes = framer.process_video("input_video.mp4", algorithm="histogram_comparison", output_dir="keyframes")
```

This will save the keyframes in the `keyframes` directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
