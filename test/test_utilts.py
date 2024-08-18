import unittest
import os
import cv2
from keyframe.utils import read_video, export_frame


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.video_path = "test_video.mp4"  # Replace with a path to a test video file
        self.output_path = "test_output.jpg"

    def test_read_video(self):
        frames = read_video(self.video_path)
        self.assertIsInstance(frames, list)
        self.assertGreater(len(frames), 0)

    def tearDown(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)


if __name__ == "__main__":
    unittest.main()
