import numpy as np
import cv2
import argparse
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True,
        help = "Give the path to the image")
arg = vars(ap.parse_args())

image = cv2.imread(arg["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corner = cv2.goodFeaturesToTrack(gray,30,0.01,10)
corner = np.int0(corner)

for i in corner:
    x,y = i.ravel()
    cv2.circle(image,(x,y),3,255,-1)

plt.imshow(image),plt.show()
