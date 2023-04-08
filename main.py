import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

while True:
    check1, frame1 = video.read()
    cv2.imshow("MY VIDEO",frame1)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
