#BASIC FUNCTIONS
import cv2
import numpy as np

img = cv2.imread('murtazas-course/resources/lena.jpg')
kernel = np.ones((5,5), np.uint8)

# convert image to gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur image (the kernel size must be odd)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

# edge detection (remember to tune the threshold 1 and 2)
imgCanny = cv2.Canny(img, 150, 200)

# dilation image (join the edges)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# erode image (separate the edges)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dialation Image', imgDialation)
cv2.imshow('Eroded Image', imgDialation)



cv2.waitKey(0)