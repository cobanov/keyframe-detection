import unittest
import numpy as np
from keyframe.framer import Framer


class TestFramer(unittest.TestCase):

    def setUp(self):
        # Create a Framer instance and sample frames
        self.framer = Framer()
        self.frames = [
            np.zeros((100, 100, 3), dtype=np.uint8),
            np.ones((100, 100, 3), dtype=np.uint8) * 255,
        ]

    def test_process_video(self):
        # Test processing a video
        keyframes, indices = self.framer.process_video(
            "asset/short.mp4", algorithm="pixelwise"
        )
        self.assertGreater(len(keyframes), 0)


if __name__ == "__main__":
    unittest.main()
