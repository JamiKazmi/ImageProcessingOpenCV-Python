import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/messi5.jpg', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
# Changing the value in uinsigned 
# int8 which is for output using numpy
lap = np.uint8(np.absolute(lap))

# Sobel X and Y method
# Here the first 1 is dx which is order of derivative X (Direction X)
# And the 0 is dy which is order of derivative Y (Direction Y)
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

# Changing the value in uinsigned 
# int8 which is for output using numpy
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Sobel XY combined method
sobelCombined = cv.bitwise_or(sobelX, sobelY)

# Canny edge method
edges = cv.Canny(img, 100, 200)

titles = [
    'Image',
    'Laplacian',
    'SobelX',
    'SobelY',
    'sobelCombined',
    'CannyEgde'
]

images = [
    img,
    lap,
    sobelX,
    sobelY,
    sobelCombined,
    edges
]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
