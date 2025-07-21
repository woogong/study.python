import cv2 as cv
import numpy as np

img1 = np.zeros((300, 300), dtype=np.uint8)
cv.rectangle(img1, (50, 50), (200, 200), 255, -1)

img2 = np.zeros((300, 300), dtype=np.uint8)
cv.circle(img2, (150, 150), 100, 255, -1)

bw_and = cv.bitwise_and(img1, img2)
bw_or = cv.bitwise_or(img1, img2)
bw_xor = cv.bitwise_xor(img1, img2)
bw_not = cv.bitwise_not(img1)

cv.imshow("img", bw_not)

k = cv.waitKey(0)