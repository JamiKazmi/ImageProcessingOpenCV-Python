import cv2 as cv
import numpy as np


def nothing(x):
    pass


# capture video from camera
cap = cv.VideoCapture(0)

# creating a window and trackbars
cv.namedWindow('Tracking')
cv.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    _, frame = cap.read()
    # frame = cv.imread('images/smarties.png')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Getting values of trackbars
    l_h = cv.getTrackbarPos('LH', 'Tracking')
    l_s = cv.getTrackbarPos('LS', 'Tracking')
    l_v = cv.getTrackbarPos('LV', 'Tracking')

    u_h = cv.getTrackbarPos('UH', 'Tracking')
    u_s = cv.getTrackbarPos('US', 'Tracking')
    u_v = cv.getTrackbarPos('UV', 'Tracking')

    # upper and lower limet for the blue color
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # creating a mask
    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow('Image', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', res)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
