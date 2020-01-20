import cv2 as cv
import numpy as np

cap = cv.VideoCapture('images/vtest.avi')
fg_bg = cv.createBackgroundSubtractorKNN(detectShadows=False)

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fg_mask = fg_bg.apply(frame)

    cv.imshow('Frame', frame)
    cv.imshow('Fg Mask Frame', fg_mask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv.destroyAllWindows()
