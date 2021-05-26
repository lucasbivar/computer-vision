#WARP PERSPECTIVE
import cv2
import numpy as np

img = cv2.imread('murtazas-course/resources/cards.png')
(height, width) = 350, 250
# pts1 = [upper left corner, upper right corner, bottom right corner, bottom left corner]
pts1 = np.float32([[70,146],[189, 127], [230, 294], [101, 320]])
pts2 = np.float32([[0,0], [width,0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Image Cropped with Perspective", imgOutput)
cv2.waitKey(0)