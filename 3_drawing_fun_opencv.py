import cv2 as cv
import numpy as np

# img = cv.imread('images/lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

# Simlpe line
img = cv.line(img, (0, 0), (255, 255), (0, 255, 0), 10)

# Arrowed Line
img = cv.arrowedLine(img, (0, 0), (260, 260), (255, 0, 0), 3)

# Rectangle
img = cv.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 2)

# Circle
img = cv.circle(img, (447, 63), 63, (0, 255, 0), -1)

# Putting text on an image
font = cv.FONT_HERSHEY_SIMPLEX      # Font-style
img = cv.putText(img, 'Open CV', (10, 500), font, 3, (110, 220, 210), 5, cv.LINE_AA)

cv.imshow('Image', img)

cv.waitKey(0)
cv.destroyAllWindows()
