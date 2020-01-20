import cv2 as cv
import numpy as np

img = cv.imread('images/road.jpg')
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(grayImg, 110, 255, apertureSize=3)
cv.imshow('Edges', edges)
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=2, maxLineGap=5)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
