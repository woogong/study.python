import cv2 as cv
import sys

fileName = input("File Name : ")
filePath = "/Users/batang/Study/python_opencv/resources/images/" + fileName

img = cv.imread(filePath)
if img is None:
    sys.exit(f"The file {filePath} is not exist")

print(f"Image : {img.shape}")

cv.imshow("show image", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("/Users/batang/Study/python_opencv/resources/targets/" + fileName, img)


