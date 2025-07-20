import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/messi2.jpg")
assert img is not None, "file could not be read"

# ROI : Region Of Interest
face = img[120:500, 1100:1400]

cv.imshow("Messi", face)
k = cv.waitKey(0)

# split
b, g, r = cv.split(img)
#cv.imshow("Blue", b)
#k = cv.waitKey(0)

#cv.imshow("Blue", g)
#k = cv.waitKey(0)

#cv.imshow("Blue", r)
#k = cv.waitKey(0)

img_weird = cv.merge((b, g, r))
cv.imshow("Weird", img_weird)
k = cv.waitKey(0)

