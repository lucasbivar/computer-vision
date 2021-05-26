# RESIZING AND CROPPING
# in opencv the origin is in upper left corner
import cv2
import numpy as np

img = cv2.imread('murtazas-course/resources/lambo.png')

print(img.shape) # (299, 416, 3) -> (height, width, channels)

# resize image
imgResize = cv2.resize(img, (832, 600)) 
print(imgResize.shape) # (832, 600, 3) -> (height, width, channels)

# crop image (height and width)
imgCropped = img[0:200, 200:500]

cv2.imshow('Image', img)
cv2.imshow('Image Resized', imgResize)
cv2.imshow('Image Cropped', imgCropped)

cv2.waitKey(0)