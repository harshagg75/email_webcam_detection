import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None

while True:
    check1, frame1 = video.read()
    gray_frame = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame=gray_frame_gau

    delta_frame = cv2.absdiff(first_frame,gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame,65,255,cv2.THRESH_BINARY)[1]
    del_frame = cv2.dilate(thresh_frame,None , iterations =2)


    contours, check = cv2.findContours(del_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour)<10000:
            continue
        x, y, w, h =cv2.boundingRect(contour)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0))



    cv2.imshow("Video", frame1)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()