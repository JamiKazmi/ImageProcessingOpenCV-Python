import cv2 as cv
import numpy as np

img = cv.imread('images/opencv-logo.png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print('No. of contours = ' + str(len(contours)))
# print(contours[0]) # showing the value of contours index 1

cv.drawContours(img, contours, -1, (0, 255, 255), 3)

cv.imshow('Image', img)
# cv.imshow('Gray Image', imgray)

cv.waitKey(0)
cv.destroyAllWindows()
