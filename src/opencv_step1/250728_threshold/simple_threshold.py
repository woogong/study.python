import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/gogh1.jpg", cv.IMREAD_GRAYSCALE)

ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow("original", img)
cv.imshow("binary", thresh1)
cv.imshow("binary_inv", thresh2)
cv.imshow("trunc", thresh3)
cv.imshow("tozero", thresh4)
cv.imshow("tozero_inv", thresh5)

cv.waitKey(0)
cv.destroyAllWindows()