import numpy as py
import cv2
from matplotlib import pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--image", required = True,
        help = "Path to image")
arg = vars(ap.parse_args())

image = cv2.imread(arg["image"])

orb = cv2.ORB()


