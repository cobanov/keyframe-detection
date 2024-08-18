import os
import shutil
import unittest

from your_package_name.framer import Framer
from your_package_name.utils import read_video


class TestFramer(unittest.TestCase):

    def setUp(self):
        self.framer = Framer()
        self.video_path = "test_video.mp4"
        self.output_dir = "test_output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_process_video(self):
        # Assuming read_video function returns some mock frames for testing
        frames = read_video(self.video_path)
        self.framer.process_video(self.video_path, "pixelwise", self.output_dir)
        self.assertTrue(os.path.exists(self.output_dir))

    def test_process_frames(self):
        # Test with mock frames
        frames = [frame for frame in range(5)]  # Replace with actual mock frames
        self.framer.process_frames(frames, "pixelwise", self.output_dir)
        self.assertTrue(os.path.exists(self.output_dir))


if __name__ == "__main__":
    unittest.main()
