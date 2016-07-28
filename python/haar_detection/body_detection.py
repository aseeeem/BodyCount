import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser(description="Imports a file to detect")
ap.add_argument("-i", "--image", required = True,
        help = "Usage is --image /path/to/file")
arg = vars(ap.parse_args())

image = cv2.imread(arg["image"])

body_cascade = cv2.CascadeClassifier('./haarcascade_upperbody.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bodys = body_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in bodys:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
