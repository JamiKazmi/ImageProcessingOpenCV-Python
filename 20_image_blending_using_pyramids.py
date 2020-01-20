import cv2 as cv
import numpy as np

apple = cv.imread('images/apple.jpg')
orange = cv.imread('images/orange.jpg')
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
# print(apple.shape)
# print(orange.shape)

# generating gaussian pyramid for apple
apple_copy = apple.copy()
gaussPyr_apple = [apple_copy]
for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gaussPyr_apple.append(apple_copy)

# generating gaussian pyramid for orange
orange_copy = orange.copy()
gaussPyr_orange = [orange_copy]
for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gaussPyr_orange.append(orange_copy)

# generating laplacian pyramid for apple
apple_copy = gaussPyr_apple[5]
lapPyr_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gaussPyr_apple[i])
    laplacian = cv.subtract(gaussPyr_apple[i-1], gaussian_extended)
    lapPyr_apple.append(laplacian)

# generating laplacian pyramid for orange
orange_copy = gaussPyr_orange[5]
lapPyr_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gaussPyr_orange[i])
    laplacian = cv.subtract(gaussPyr_orange[i-1], gaussian_extended)
    lapPyr_orange.append(laplacian)

# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lapPyr_apple, lapPyr_orange):
    n += 1
    cols, rows, channels = apple_lap.shape
    laplacian = np.hstack((
        apple_lap[:, 0:int(cols/2)],
        orange_lap[:, int(cols/2):]
    ))
    apple_orange_pyramid.append(laplacian)

# Now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(
        apple_orange_pyramid[i], apple_orange_reconstruct
    )

cv.imshow('Apple', apple)
cv.imshow('Orange', orange)
cv.imshow('Apple_Orange', apple_orange)
cv.imshow('Apple_Orange_Reconstruct', apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()
