import cv2 as cv
import numpy as np

#img = cv.imread("../../../resources/messi1.jpg", cv.IMREAD_GRAYSCALE)
#rows, columns = img.shape
img = cv.imread("../../../resources/messi1.jpg", cv.IMREAD_COLOR_BGR)
rows, columns = img.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])
dest = cv.warpAffine(img, M, (columns, rows))

cv.imshow("img", dest)
cv.waitKey(0)
cv.destroyAllWindows()