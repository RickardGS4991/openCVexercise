import numpy as np
import cv2

kernel = np.ones((5, 5), np.uint8)

videoSource = 0

cap = cv2.VideoCapture(videoSource)

_, img = cap.read()
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    cv2.imshow("HSV", imgHSV)
    if cv2.waitKey(1) & 0xFF == 27:
        break
