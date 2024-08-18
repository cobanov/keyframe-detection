import unittest
import cv2
import numpy as np
from keyframe.algorithms import (
    pixelwise,
    background_subtraction,
    optical_flow,
    histogram_comparison,
    sift_matching,
    mean_squared_error,
    phase_correlation,
)


class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.frame1 = cv2.imread(
            "test_frame_1.jpg"
        )  # Replace with a path to a test frame
        self.frame2 = cv2.imread(
            "test_frame_2.jpg"
        )  # Replace with a path to a test frame

    def test_pixelwise(self):
        result = pixelwise(self.frame1, self.frame2)
        self.assertIsInstance(result, bool)

    def test_background_subtraction(self):
        result = background_subtraction(self.frame1, self.frame2)
        self.assertIsInstance(result, bool)

    def test_optical_flow(self):
        result = optical_flow(self.frame1, self.frame2)
        self.assertIsInstance(result, bool)

    def test_histogram_comparison(self):
        result = histogram_comparison(self.frame1, self.frame2)
        self.assertIsInstance(result, bool)

    def test_sift_matching(self):
        result = sift_matching(self.frame1, self.frame2)
        self.assertIsInstance(result, bool)

    def test_mean_squared_error(self):
        result = mean_squared_error(self.frame1, self.frame2)
        self.assertIsInstance(result, bool)

    def test_phase_correlation(self):
        result = phase_correlation(self.frame1, self.frame2)
        self.assertIsInstance(result, bool)


if __name__ == "__main__":
    unittest.main()
