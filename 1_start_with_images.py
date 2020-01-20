import cv2 as cv
import numpy as np

img = cv.imread('images/lena.jpg', 1)
print(img)
cv.imshow('Image', img)

k = cv.waitKey(0) & 0xFF    # (& 0xFF) for 64bit machine

if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('images/lena_copy.png', img)
    cv.destroyAllWindows()
