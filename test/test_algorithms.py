import unittest

import cv2
import numpy as np
from your_package_name.algorithms import (background_subtraction,
                                          histogram_comparison,
                                          mean_squared_error, optical_flow,
                                          phase_correlation, pixelwise,
                                          sift_matching)


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        # Create two dummy frames for testing
        self.frame1 = np.zeros((100, 100, 3), dtype=np.uint8)
        self.frame2 = np.zeros((100, 100, 3), dtype=np.uint8)
        self.frame2[50:, 50:] = (
            255  # Change part of the frame2 to simulate a difference
        )

    def test_pixelwise(self):
        self.assertTrue(pixelwise(self.frame1, self.frame2))

    def test_background_subtraction(self):
        self.assertFalse(background_subtraction(self.frame1, self.frame2))

    def test_optical_flow(self):
        self.assertFalse(optical_flow(self.frame1, self.frame2))

    def test_histogram_comparison(self):
        self.assertTrue(histogram_comparison(self.frame1, self.frame2))

    def test_sift_matching(self):
        self.assertFalse(sift_matching(self.frame1, self.frame2))

    def test_mean_squared_error(self):
        self.assertTrue(mean_squared_error(self.frame1, self.frame2))

    def test_phase_correlation(self):
        self.assertFalse(phase_correlation(self.frame1, self.frame2))


if __name__ == "__main__":
    unittest.main()
