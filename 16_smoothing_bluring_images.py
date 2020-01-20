import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.uint8) / 25
dest = cv.filter2D(img, -2, kernel)
blur = cv.blur(img, (5, 5))
gBlur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)

titles = [
    'Image',
    '2D Convolution',
    'Blur',
    'GaussianBlur',
    'Median',
    'bilateralFilter'
]
images = [
    img,
    dest,
    blur,
    gBlur,
    median,
    bilateralFilter
]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
