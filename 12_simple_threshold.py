import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/gradient.png')

# Thresholding binary
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# Thresholding binary inverse
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# Thresholding trunc
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
# Thresholding To Zero
_, th4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
# Thresholding To Zero inverse
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = [
    'Image',
    'BINARY',
    'BINARY_INV',
    'TRUNC',
    'TOZERO',
    'TOZERO_INV'
]

images = [
    img,
    th1,
    th2,
    th3,
    th4,
    th5
]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# cv.imshow('Image', img)
# cv.imshow('Th1', th1)
# cv.imshow('Th2', th2)
# cv.imshow('Th3', th3)
# cv.imshow('Th4', th4)
# cv.imshow('Th5', th5)
# cv.waitKey(0)
# cv.destroyAllWindows()

plt.show()
