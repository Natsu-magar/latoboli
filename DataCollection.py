import cv2
from cvzone.HandTrackingModule import HandDetector

import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
        imgCrop = img[y-offset:y + h+offset, x-offset:x + w+offset]

        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgWhite[0:imgResize.shape[0], 0:imgResize.shape[1]] = imgResize
        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgWhite[0:imgResize.shape[0], 0:imgResize.shape[1]] = imgResize

        cv2.imshow("Cropped Image", imgCrop)
        cv2.imshow("white background", imgWhite)

    cv2.imshow("Hand Image", img)
    cv2.waitKey(1)