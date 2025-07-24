import cv2 as cv
import numpy as np

cap = cv.VideoCapture("../../../resources/yeongun1.mp4")

width = 640
height = int(1280 * (640 / 1920))
fps = cap.get(cv.CAP_PROP_FPS)
fourcc = cap.get(cv.CAP_PROP_FOURCC)
output_fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("../../../resources/converted.avi", output_fourcc, fps, (width, height))

if not cap.isOpened or not out.isOpened():
    print(f"Error: Could not open files")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        resized = cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)
        #resized = cv.flip(resized, 1)
        #gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)

        out.write(resized)
        
        cv.imshow("video", resized)
        if cv.waitKey(1) == ord('q'):
            break

cap.release()
out.release()
cv.destroyAllWindows()
