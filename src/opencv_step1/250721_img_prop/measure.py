import cv2 as cv

#cv.setUseOptimized(False)
print(f"useOptimzed : {cv.useOptimized()}")

img = cv.imread("../../../resources/messi2.jpg")
assert img is not None, "image not found"

e1 = cv.getTickCount()

for i in range(5, 49, 2):
    img = cv.medianBlur(img, i)

e2 = cv.getTickCount()
time = (e2 - e1) / cv.getTickFrequency()
print(f"time : {time}")

cv.imshow("blur", img)
k = cv.waitKey(0)