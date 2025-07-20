import cv2 as cv
import numpy as np

img = cv.imread("../../../resources/messi1.jpg")
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[100, 100]
print( px )

blue = img[100, 100, 0]
print( blue )

img[100, 100] = [255, 255, 255]

print(f"img.shape : {img.shape}")
print(f"img.size : {img.size}")
print(f"img.dtype : {img.dtype}")
