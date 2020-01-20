import cv2 as cv
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv.rectangle(img1, (200, 0),(300, 100), (255, 255, 255), -1)
img2 = cv.imread('images/black-white.jpg')

# bitwise operations
# bitAnd = cv.bitwise_and(img1, img2)
# bitOr = cv.bitwise_or(img1, img2)
# bitXor = cv.bitwise_xor(img1, img2)
bitNot1 = cv.bitwise_not(img1)
bitNot2 = cv.bitwise_not(img2)

cv.imshow('Img1', img1)
cv.imshow('Img2', img2)
# cv.imshow('bitAnd', bitAnd)
# cv.imshow('bitOr', bitOr)
# cv.imshow('bitXor', bitXor)
cv.imshow('bitNot1', bitNot1)
cv.imshow('bitNot2', bitNot2)

cv.waitKey(0)
cv.destroyAllWindows()
