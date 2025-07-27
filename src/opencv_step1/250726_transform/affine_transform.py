import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/messi2.jpg")
rows, cols, channel = img.shape
img = cv.resize(img, (cols // 2, rows // 2), interpolation=cv.INTER_CUBIC)
rows, cols, channel = img.shape
print(f"{rows} {cols}")

pts1 = np.float32([[50, 50], [250, 50], [50, 150]])
pts2 = np.float32([[50, 50], [250, 50], [100, 150]])

M = cv.getAffineTransform(pts1, pts2)

dest = cv.warpAffine(img, M, (cols, rows))

cv.imshow("dst", dest)
cv.waitKey(0)
cv.destroyAllWindows()