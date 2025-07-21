import cv2 as cv

img1 = cv.imread("../../../resources/gogh1.jpg")
img2 = cv.imread("../../../resources/messi1.jpg")

print(f"img1 : {img1.shape}")
print(f"img2 : {img2.shape}")

img1Resized = img1[0:280, 0:450]


dst = cv.addWeighted(img1Resized, 0.4, img2, 0.8, 0)

cv.imshow("added", dst)
k = cv.waitKey(0)

cv.destroyAllWindows()