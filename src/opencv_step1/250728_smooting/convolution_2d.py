import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/messi1.jpg")

kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)

cv.imshow("original", img)
cv.imshow("filtered", dst)

cv.waitKey(0)
cv.destroyAllWindows()