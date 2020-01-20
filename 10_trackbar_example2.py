import numpy as np
import cv2 as cv


def nothing(x):
    print(x)


cv.namedWindow('Image')

# Creating trackbars
cv.createTrackbar('CPos', 'Image', 10, 400, nothing)

# Creating switch using trackbar
switch = 'Color/Gray'
cv.createTrackbar(switch, 'Image', 0, 1, nothing)

while True:
    img = cv.imread('images/lena.jpg')
    pos = cv.getTrackbarPos('CPos', 'Image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (10, 100), font, 3, (0, 255, 255), 2)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    
    s = cv.getTrackbarPos(switch, 'Image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('Image', img)

cv.destroyAllWindows()
