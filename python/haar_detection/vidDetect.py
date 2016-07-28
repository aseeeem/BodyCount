import cv2
import numpy as np

vid=cv2.VideoCapture('/home/asim/Documents/BodyCount/videofiles/withPeople/MVI_0043.MP4')
body_cascade=cv2.CascadeClassifier('/home/asim/Downloads/opencv-3.1.0/data/haarcascades/haarcascade_upperbody.xml')
head_cascade=cv2.CascadeClassifier('/home/asim/Downloads/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
side_cascade=cv2.CascadeClassifier('/home/asim/Downloads/opencv-3.1.0/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
while vid.isOpened():
    ret, frame = vid.read()
    # Needed to downscale the video for faster processing
    # Was taking too long at max res
    # These next lines shorten the resolution to 800 width
    # The height auto adjusts
    ratio = 1600 / frame.shape[1]
    dim = (1600, int(frame.shape[0] * ratio))
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray, 1.3, 5)
    head = head_cascade.detectMultiScale(gray, 1.3, 5)
    profile = side_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in body:
        cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = resized[y:y+h, x:x+w]
    for (z, c, b, n) in head:
        cv2.rectangle(resized, (z, c), (z+b, c+n), (0, 0, 255), 2)
        roi_color = resized[c:c+n, z:z+b]
    for (px, py, pw, ph) in profile:
        cv2.rectangle(resized, (px, py), (px+pw, pw+ph), (255, 0, 0), 2)
        roi_color = resized[py:py+ph, px:px+pw]
    cv2.imshow('resized', resized)
    if cv2.waitKey(1) &  0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
