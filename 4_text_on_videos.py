import cv2 as cv
import datetime
import numpy as np

cap = cv.VideoCapture(0)

print(cap.get(3))   # width of frame
print(cap.get(4))   # height of frame

# setting width and height of frame
# cap.set(3, 1280)
# cap.set(4, 720)

# print(cap.get(3))   # width of frame
# print(cap.get(4))   # height of frame

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        font = cv.FONT_HERSHEY_SIMPLEX
        # text = 'Width : ' + str(cap.get(3)) + ' Height : ' + str(cap.get(4))
        dated = str(datetime.datetime.now())
        frame = cv.putText(
            frame,
            dated,
            (20, 30),
            font, 1,
            (0, 255, 255), 2,
            cv.LINE_AA
            )
        cv.imshow('Video', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
