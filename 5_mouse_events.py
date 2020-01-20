import cv2 as cv
import numpy as np

# It will show all the events in opencv
# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 1)
        cv.imshow('Image', img)

    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 0]
        red = img[x, y, 0]
        font = cv.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 1)
        cv.imshow('Image', img)


# Black Image
# img = np.zeros([520, 520, 3], np.uint8)

img = cv.imread('images/messi5.jpg', 1)
cv.imshow('Image', img)

cv.setMouseCallback('Image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
