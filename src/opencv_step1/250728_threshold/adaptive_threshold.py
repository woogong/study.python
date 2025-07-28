import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/gogh1.jpg", cv.IMREAD_GRAYSCALE)
img = cv.medianBlur(img, 5)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


cv.imshow("original", img)
cv.imshow("simple", th1)
cv.imshow("mean", th2)
cv.imshow("gausian", th3)

cv.waitKey(0)
cv.destroyAllWindows()