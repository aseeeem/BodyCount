import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser(description="Imports a file to detect")
ap.add_argument("-i", "--image", required = True,
        help = "Usage is --image /path/to/file")
arg = vars(ap.parse_args())

image = cv2.imread(arg["image"])

profile_cascade=cv2.CascadeClassifier('/home/asim/Downloads/opencv-3.1.0/data/haarcascades/haarcascade_profileface.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces=profile_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
