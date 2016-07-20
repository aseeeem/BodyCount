import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser(description="Imports a file to detect")
ap.add_argument("-i", "--image", required = True,
        help = "Usage is --image /path/to/file")
arg = vars(ap.parse_args())

image = cv2.imread(arg["image"])

face_cascade=cv2.CascadeClassifier('/home/asim/Documents/BodyCount/python/haar_detection/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()