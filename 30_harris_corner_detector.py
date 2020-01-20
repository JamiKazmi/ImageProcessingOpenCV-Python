import cv2 as cv
import numpy as np

img = cv.imread('images/chessboard.png')
cv.imshow('Image', img)

gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_image = np.float32(gray_image)
dst = cv.cornerHarris(gray_image, 2, 3, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv.imshow('Result', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()
