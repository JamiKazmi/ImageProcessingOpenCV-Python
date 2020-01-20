import cv2 as cv
import numpy as np

img = cv.imread('images/messi5.jpg')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('images/messi_face.jpg', 0)
w, h = template.shape[::-1]

res = cv.matchTemplate(imgGray, template, cv.TM_CCORR_NORMED)
print(res)
threshold = 0.96
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
