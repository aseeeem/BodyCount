import cv2
import numpy as np

vid=cv2.VideoCapture('/home/asim/Documents/BodyCount/videofiles/withPeople/MVI_0043.MP4')
face_cascade=cv2.CascadeClassifier('/home/asim/Documents/BodyCount/python/haar_detection/haarcascade_frontalface_default.xml')
while vid.isOpened():
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) &  0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
