import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


cv.namedWindow('Trackbars')
cv.createTrackbar('th1', 'Trackbars', 100, 500, nothing)
cv.createTrackbar('th2', 'Trackbars', 200, 500, nothing)

img = cv.imread('images/messi5.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Image', img)

while True:
    th1 = cv.getTrackbarPos('th1', 'Trackbars')
    th2 = cv.getTrackbarPos('th2', 'Trackbars')
    canny = cv.Canny(img, th1, th2)
    cv.imshow('Canny', canny)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
