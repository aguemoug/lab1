# Importing the OpenCV library
import cv2 as cv
import numpy as np

# Importing the matplotlib library to show the images
from matplotlib import pyplot as plt # w use plt in rather than pyplot 

# Reading the image using imread() function
img = cv.imread('cofee.jpg')
  
# Extracting the height and width of an image
h, w = img.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))


cv.imshow("Image",img)
cv.waitKey(00) # waits until you press a key and closes the window.
