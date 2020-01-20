import cv2 as cv
import numpy as np

img = cv.imread('images/lena.jpg')
layer = img.copy()
gaussianPyramid = [layer]

# pyrDown method whicb reduce the resolution
for i in range(6):
    layer = cv.pyrDown(layer)
    gaussianPyramid.append(layer)
    # cv.imshow(str(i), layer)

layer = gaussianPyramid[5]
cv.imshow('Upper level gaussian pyramid', layer)
laplacianPyramid = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gaussianPyramid[i])
    laplacian = cv.subtract(gaussianPyramid[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)

cv.imshow('Original Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
