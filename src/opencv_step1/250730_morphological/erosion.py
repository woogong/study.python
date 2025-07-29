import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/j.png")
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dialation = cv.dilate(img, kernel, iterations=1)

cv.imshow("original", img)
cv.imshow("erosion", erosion)
cv.imshow("dialation", dialation)

cv.waitKey(0)
cv.destroyAllWindows()