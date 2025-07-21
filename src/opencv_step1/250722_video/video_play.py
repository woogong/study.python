import cv2 as cv

cap = cv.VideoCapture("../../../resources/yeongun1.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        print("cannot receive frame")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
