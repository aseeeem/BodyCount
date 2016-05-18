import numpy as np
import cv2

# This line defines a 300x300 array
# The '3' allocates spaces for 3 channels
# the .zeroes call initializes each value with a 0
# The dtype argument sets the data type of each value to an unsigned 8-bit int
canvas = np.zeros((300, 300, 3), dtype = "uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
# Draw line on canvas
# From 300,0 to 0,300
# Using red
# Pixel width of 3
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
