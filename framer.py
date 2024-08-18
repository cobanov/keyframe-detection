import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np


class Framer:
    def __init__(self) -> None:
        self.frame1 = bytearray()
        self.frame2 = bytearray()

    def pixelwise(self, frame1, frame2):
        difference = cv2.absdiff(frame1, frame2)
        return difference

    def backround_subtraction(self, frame1, frame2):
        fgbg = cv2.createBackgroundSubtractorMOG2()
        fgmask = fgbg.apply(frame1)
        fgmask = fgbg.apply(frame2)
        return fgmask

    def optical_flow(self, frame1, frame2, type="lucas-kanade"):
        if type == "lucas-kanade":
            flow = cv2.calcOpticalFlowPyrLK(frame1, frame2, prev_points, None)

        if type == "farneback":
            flow = cv2.calcOpticalFlowFarneback(
                frame1, frame2, None, 0.5, 3, 15, 3, 5, 1.2, 0
            )

        return flow

    def structural_similarity(self, frame1, frame2):
        score, diff = ssim(frame1, frame2, full=True)
        return score, diff

    def histogram_comparison(self, frame1, frame2):
        hist1 = cv2.calcHist([frame1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([frame2], [0], None, [256], [0, 256])
        return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    def feature_matching(self, frame1, frame2):
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(frame1, None)
        kp2, des2 = orb.detectAndCompute(frame2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        return matches

    def sift_matching(self, frame1, frame2):
        sift = cv2.SIFT_create()
        kp1, des1 = sift.detectAndCompute(frame1, None)
        kp2, des2 = sift.detectAndCompute(frame2, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        return matches

    def mean_squared_error(self, frame1, frame2):
        err = np.sum((frame1.astype("float") - frame2.astype("float")) ** 2)
        err /= float(frame1.shape[0] * frame1.shape[1])
        return err

    def block_matching(self, frame1, frame2):
        block_size = 16
        shift = 8
        search_range = 16
        block = cv2.createBlockMatching(frame1, frame2, block_size, shift, search_range)
        return block

    def phase_correlation(self, frame1, frame2):
        return cv2.phaseCorrelate(frame1, frame2)
