import argparse
import cv2

# This file will make a green square in the top right!
# Yay! 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
        help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Orignal", image)

(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: ", r, ", Green: ", g, ", Blue: ", b)

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Now see the difference!")
print("Pixel at (0,0) - Red: ", r, ", Green: ", g, ", Blue: ", b)

green = (0, 255, 0)
cv2.rectangle(image, (0, 0), (100, 100), green)
cv2.imshow("Updated", image)
cv2.waitKey(0)
