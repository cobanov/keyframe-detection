import unittest
import os
import cv2
from keyframe.framer import Framer


class TestFramer(unittest.TestCase):
    def setUp(self):
        self.framer = Framer()
        self.video_path = "asset/short.mp4"

    def test_process_video(self):
        keyframes, indices = self.framer.process_video(
            self.video_path, algorithm="pixelwise", output_dir="test_output"
        )
        self.assertIsInstance(keyframes, list)
        self.assertIsInstance(indices, list)
        self.assertTrue(os.path.exists("test_output"))

    def tearDown(self):
        if os.path.exists("test_output"):
            for file_name in os.listdir("test_output"):
                os.remove(os.path.join("test_output", file_name))
            os.rmdir("test_output")


if __name__ == "__main__":
    unittest.main()
