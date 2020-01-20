import cv2 as cv
import numpy as np

img = cv.imread('images/messi5.jpg')
img2 = cv.imread('images/opencv-logo.png')

print(img.shape)    # Return a tuple of numbers of rows, columns and channels
print(img.size)     # Return total numbers of pixels is accessed
print(img.dtype)    # Return image data type is obtained

b, g, r = cv.split(img)
img = cv.merge((b, g, r))


# ROI of an Image (Reagon of intrest)
# ball = img[280:340, 330:390]
# img[70:130, 200:260] = ball
# head = img[70:130, 200:260]
# img[280:340, 330:390] = head

# Resizeing images
img = cv.resize(img, (720, 480))
img2 = cv.resize(img2, (720, 480))

# Adding 2 images
# dest = cv.add(img, img2)

# Adding 2 images per weight
dest = cv.addWeighted(img, .5, img2, .5, 0)

cv.imshow('Image', dest)

cv.waitKey(0)
cv.destroyAllWindows()
