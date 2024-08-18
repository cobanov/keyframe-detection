import cv2
import numpy as np


def pixelwise(frame1, frame2, threshold=0.9):
    difference = cv2.absdiff(frame1, frame2)
    gray_diff = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    mean_diff = np.mean(gray_diff)
    normalized_diff = mean_diff / 255
    similarity = 1 - normalized_diff

    return similarity < threshold


def background_subtraction(frame1, frame2, threshold=0.2):
    fgbg = cv2.createBackgroundSubtractorMOG2()
    fgmask1 = fgbg.apply(frame1)
    fgmask2 = fgbg.apply(frame2)
    difference = cv2.absdiff(fgmask1, fgmask2)
    similarity = np.sum(difference) / (difference.size * 255)

    return similarity < threshold


def optical_flow(frame1, frame2, threshold=1.5, method="farneback"):
    if method == "farneback":
        flow = cv2.calcOpticalFlowFarneback(
            cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY),
            cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY),
            None,
            0.5,
            3,
            15,
            3,
            5,
            1.2,
            0,
        )
        magnitude, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        similarity = np.mean(magnitude)
        return similarity > threshold
    else:
        raise ValueError(f"Unsupported optical flow method: {method}")


def histogram_comparison(frame1, frame2, threshold=0.5):
    hist1 = cv2.calcHist([frame1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([frame2], [0], None, [256], [0, 256])
    comparison_score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    similarity = 1 - comparison_score
    return similarity > threshold


def sift_matching(frame1, frame2, threshold=10):
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(frame1, None)
    kp2, des2 = sift.detectAndCompute(frame2, None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]
    return len(good_matches) < threshold


def mean_squared_error(frame1, frame2, threshold=4000):
    err = np.sum((frame1.astype("float") - frame2.astype("float")) ** 2)
    err /= float(frame1.shape[0] * frame1.shape[1])
    return err > threshold


def phase_correlation(frame1, frame2, threshold=1.7):
    gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    float_frame1 = np.float32(gray_frame1)
    float_frame2 = np.float32(gray_frame2)
    shift, _ = cv2.phaseCorrelate(float_frame1, float_frame2)
    magnitude = np.linalg.norm(shift)
    return magnitude > threshold
