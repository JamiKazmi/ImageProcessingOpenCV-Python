import cv2 as cv
import numpy as np

img = cv.imread('images/shapes.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(
    imgGray, 200, 255,
    cv.THRESH_BINARY
)
contours, _ = cv.findContours(
    thresh,
    cv.RETR_TREE,
    cv.CHAIN_APPROX_NONE
)

for contour in contours:
    approx = cv.approxPolyDP(
        contour,
        0.01 * cv.arcLength(contour, True),
        True
    )

    cv.drawContours(
        img, [approx],
        0, (0, 0, 255), 2
    )
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3:
        cv.putText(
            img, 'Triangle',
            (x, y),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2
        )

    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectRatio = float(w) / h
        print(aspectRatio)

        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv.putText(
                img, 'Square',
                (x, y),
                cv.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2
            )
        else:
            cv.putText(
                img, 'Rectangle',
                (x, y),
                cv.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2
            )

    elif len(approx) == 5:
        cv.putText(
            img, 'Pantagon',
            (x, y),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2
        )

    elif len(approx) == 10:
        cv.putText(
            img, 'Star',
            (x, y),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2
        )

    else:
        cv.putText(
            img, 'Circle',
            (x, y),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 0), 2
        )

cv.imshow('Shapes', img)

cv.waitKey(0)
cv.destroyAllWindows()
