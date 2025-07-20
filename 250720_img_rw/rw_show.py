import cv2 as cv
import sys

img = cv.imread("../resources/gogh1.jpg")
if img is None:
    sys.exit(f"The file is not exist")

print(f"Image : {img.shape}")

cv.imshow("show image", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("../resources/gogh1_dup.jpg", img)


