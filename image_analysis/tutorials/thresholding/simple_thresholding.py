import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
        help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
#cv2.imshow("Grayed and Blurred", image)
# Lower numbers result in lower threshold
# For brighter images, use higher thresholds
(T, thresh) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)
#cv2.imshow("threshold binary", thresh)
(T, threshInverse) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow("Threshold binary inverse", threshInverse)
finalImage = cv2.bitwise_and(image, image, mask = threshInverse)
#cv2.waitKey(0)
filename = input("What is this image going to be called: ")
filename = "images/" + filename.strip() + ".jpg"
if cv2.imwrite(filename, finalImage):
    print("Successfully wrote ",filename)

