import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/lena.jpg')
cv.imshow('Image', img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
