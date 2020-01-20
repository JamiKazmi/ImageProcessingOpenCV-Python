import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((4, 4), np.uint8)

dilation = cv.dilate(mask, kernel, iterations=2)
erosion = cv.erode(mask, kernel)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
morphGradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
topHat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel)

titles = [
    'Image',
    'Mask',
    'Dilation',
    'Erosion',
    'Opening',
    'Closing',
    'morphGradient',
    'topHat'
]

images = [
    img,
    mask,
    dilation,
    erosion,
    opening,
    closing,
    morphGradient,
    topHat
]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
