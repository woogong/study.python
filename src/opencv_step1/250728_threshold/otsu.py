import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/gogh1.jpg", cv.IMREAD_GRAYSCALE)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)


cv.imshow("original", img)
cv.imshow("binaray", th1)
cv.imshow("otsu", th2)
cv.imshow("blur", blur)
cv.imshow("blur + otsu", th3)

cv.waitKey(0)
cv.destroyAllWindows()