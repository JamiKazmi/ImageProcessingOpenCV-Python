import cv2 as cv
import numpy as np

img = cv.imread('images/pic1.png')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray_image, 22, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, 255, -1)

cv.imshow('Image', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()
