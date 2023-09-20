import numpy as np
import cv2
import random

while True:
    number = random.randint(0, 100)
    name = "webcam" + str(number) + ".jpg"
    cap = cv2.VideoCapture(0)
    read, frame = cap.read()
    cv2.imwrite(name, frame)
    if read == True:
        cv2.imshow('webcam.jpg', frame)
        print("Photo successfully take it")
    else:
        print('cannot take photo')
