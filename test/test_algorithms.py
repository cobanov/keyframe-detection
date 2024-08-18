import unittest
import numpy as np
import cv2
from keyframe import algorithms


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        # Create two simple test frames
        self.frame1 = np.zeros((100, 100, 3), dtype=np.uint8)
        self.frame2 = np.ones((100, 100, 3), dtype=np.uint8) * 255

    def test_pixelwise(self):
        # Test pixelwise algorithm
        result = algorithms.pixelwise(self.frame1, self.frame2, threshold=0.9)
        self.assertTrue(result)

    def test_background_subtraction(self):
        # Test background subtraction algorithm
        result = algorithms.background_subtraction(
            self.frame1, self.frame2, threshold=0.2
        )
        self.assertTrue(result)

    def test_optical_flow(self):
        # Test optical flow algorithm
        result = algorithms.optical_flow(self.frame1, self.frame2, threshold=1.5)
        self.assertFalse(result)

    def test_histogram_comparison(self):
        # Test histogram comparison algorithm
        result = algorithms.histogram_comparison(
            self.frame1, self.frame2, threshold=0.5
        )
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
