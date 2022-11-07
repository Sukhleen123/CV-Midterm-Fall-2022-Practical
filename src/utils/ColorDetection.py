import cv2
import numpy as np

class ColorDetection:
    def __init__(self):
        self.red_lower = np.array([0, 7, 232])
        self.red_upper = np.array([55, 255, 255])
        self.blue_lower = np.array([62, 43, 140])
        self.blue_upper = np.array([110, 255, 255])

    # Checks if more red or blue then decides if plate is red or blue
    def red_or_blue(self, color_frame):
        hsv = cv2.cvtColor(color_frame, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsv, self.red_lower, self.red_upper)
        blue_mask = cv2.inRange(hsv, self.blue_lower, self.blue_upper)
        red_contours, _ = cv2.findContours(
            red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        blue_contours, _ = cv2.findContours(
            blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(red_contours) > 0 and len(blue_contours) > 0:
            r_area = 0
            b_area = 0
            for c in red_contours:
                r_area += cv2.contourArea(c)
            for c in blue_contours:
                b_area += cv2.contourArea(c)
            if r_area > b_area:
                return 'r'
            else:
                return 'b'
        elif len(red_contours) > 0:
            return 'r'

        return 'b'

