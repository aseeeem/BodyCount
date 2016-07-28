import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
        help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
print("Width: ", image.shape[1], " pixels")
print("Height: ", image.shape[0], " pixels")
print("Channels: ", image.shape[2], " pixels")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)
