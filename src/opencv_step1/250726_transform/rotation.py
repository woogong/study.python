import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/messi1.jpg")
angle = 90
rows, cols = img.shape[:2]

#center = ((cols - 1) / 2.0, (rows - 1) / 2.0)
center = ((cols - 1), (rows - 1))
scale = 2

M = cv.getRotationMatrix2D(center, angle, 2)
dest = cv.warpAffine(img, M, (1000, 1000))

cv.imshow("img", dest)
cv.waitKey(0)
cv.destroyAllWindows()