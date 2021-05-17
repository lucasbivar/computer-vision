import cv2
import imutils
import numpy as np
from skimage.filters import threshold_local

def nothing(arg):
  pass


# image = cv2.imread("images/flower.png")
cv2.namedWindow("Testing Threshold")
cv2.createTrackbar("Low Threshold", "Testing Threshold",10, 255, nothing)
cv2.createTrackbar("High Threshold", "Testing Threshold",200, 255, nothing)
cap = cv2.VideoCapture(0)



# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
while True:
  ret, frame = cap.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blurred = cv2.GaussianBlur(gray, (5, 5), 0)

  low = int(cv2.getTrackbarPos("Low Threshold", "Testing Threshold"))
  high = int(cv2.getTrackbarPos("High Threshold", "Testing Threshold"))

  wide = cv2.Canny(blurred, low, high)

  cv2.imshow("Testing Threshold", wide)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
        break