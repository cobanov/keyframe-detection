import os
import unittest

import numpy as np
from your_package_name.utils import export_frame, read_video


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.frame = np.zeros((100, 100, 3), dtype=np.uint8)
        self.output_path = "test_frame.png"

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_read_video(self):
        # Assuming read_video returns a list of frames
        frames = read_video("test_video.mp4")
        self.assertIsInstance(frames, list)

    def test_export_frame(self):
        export_frame(self.frame, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))


if __name__ == "__main__":
    unittest.main()
