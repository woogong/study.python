import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(type(img)) 
# img의 type은 np.ndarray이다.
# OpenCV에서 이미지 타입이 별도로 있지 않다.
# 3차원 배열이 이미지다.

cv.line(img, (10, 10), (502, 502), (255, 127, 0), 5, cv.LINE_8)

cv.circle(img, (447, 63), 63, (0, 127, 255), -1, cv.LINE_AA)

cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (127, 255, 127), -1, cv.LINE_AA)

pts = np.array([[10, 30], [40, 80], [150, 200], [400, 180]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "GMDSOFT", (30, 500), font, 2, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow("img", img)

cv.waitKey(0)
cv.destroyAllWindows()