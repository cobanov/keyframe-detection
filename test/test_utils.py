
import unittest
from keyframe.utils import read_video, export_frame
import numpy as np
import os

class TestUtils(unittest.TestCase):

    def test_read_video(self):
        # Test reading a video
        frames = read_video("asset/short.mp4")
        self.assertGreater(len(frames), 0)

    def test_export_frame(self):
        # Test exporting a frame
        frame = np.zeros((100, 100, 3), dtype=np.uint8)
        output_path = "output_frame.jpg"
        export_frame(frame, output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)

if __name__ == "__main__":
    unittest.main()
