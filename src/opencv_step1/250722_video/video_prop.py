import cv2 as cv

cap = cv.VideoCapture("../../../resources/yeongun1.mp4")

if cap.isOpened():
    for i in range(0, 18):
        value = cap.get(i)
        print(f"{i} : {value}")

cap.set(3, 640)
cap.set(4, 480)
# It doesn't effect to play the video

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("cannot read frame")
        break

    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
