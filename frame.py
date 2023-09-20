import cv2
import numpy as np
import time
pTime = 0
cTime = 0

videoSource = 0

cap = cv2.VideoCapture(videoSource)

while True:
    success, img = cap.read()
    width = img.shape[1]
    height = img.shape[0]
    print(width, height)

    if success:
        # img = cv2.resize(img, (320, 160))
        img = cv2.flip(img, -1)
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
