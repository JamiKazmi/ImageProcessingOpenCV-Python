import cv2 as cv
import numpy as np

# It will show all the events in opencv
# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv.circle(img, (x, y), 3, (0, 0, 255), -1)
        myColorImg = np.zeros((512, 512, 3), np.uint8)
        myColorImg[:] = [blue, green, red]
        cv.imshow('Color', myColorImg)

        # cv.circle(img, (x, y), 3, (255, 255, 0), -1)
        # points.append((x, y))
        # if len(points) >= 2:
        #     cv.line(img, points[-1], points[-2], (255, 0, 0), 1)


# Black Image
# img = np.zeros([520, 520, 3], np.uint8)

img = cv.imread('images/lena.jpg', 1)
cv.imshow('Image', img)

points = []

cv.setMouseCallback('Image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
