from collections import deque
from imutils.video import VideoStream
import numpy as np
from pynput.keyboard import Key, Controller
import cv2
import imutils
import time

def nothing(args):
  pass

keyboard = Controller()

cap = cv2.VideoCapture(0)

colorLower = (5, 0, 0)
colorUpper = (0, 0, 0)

cv2.namedWindow("Color Tracker")
cv2.createTrackbar("H", "Color Tracker", 0, 179, nothing)
cv2.createTrackbar("S", "Color Tracker", 0, 255, nothing)
cv2.createTrackbar("V", "Color Tracker", 0, 255, nothing)

frame_rate = 15
prev = 0

while True:
  time_elapsed = time.time() - prev
  ret, frame = cap.read()

  if time_elapsed > 1./frame_rate:
    prev = time.time()
  frame = cv2.putText(frame, 'UP', (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 
                   2, (0, 255 , 0), 2, cv2.LINE_AA)
  cv2.line(frame, (0, 160), (640, 160), (0, 255, 0) ,2)

  cv2.line(frame, (0, 320), (640, 320), (0, 255, 0) ,2)
  frame = cv2.putText(frame, 'DOWN', (20, 470), cv2.FONT_HERSHEY_SIMPLEX, 
                   2, (0, 255 , 0), 2, cv2.LINE_AA)
  h = int(cv2.getTrackbarPos("H", "Color Tracker"))
  s = int(cv2.getTrackbarPos("S", "Color Tracker"))
  v = int(cv2.getTrackbarPos("V", "Color Tracker"))

  colorLower = (h-20, s-20, v-50)
  colorUpper = (h+20, s+20, v+50)

  # resize the frame, blur it, and convert it to the HSV
  # color space
  frame = imutils.resize(frame, width=600)
  blurred = cv2.GaussianBlur(frame, (11, 11), 0)
  hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
  
  # construct a mask for the color "green", then perform
  # a series of dilations and erosions to remove any small
  # blobs left in the mask
  mask = cv2.inRange(hsv, colorLower, colorUpper)
  mask = cv2.erode(mask, None, iterations=2)
  mask = cv2.dilate(mask, None, iterations=3)
  cv2.imshow("operations", mask)

  # find contours in the mask and initialize the current
	# (x, y) center of the ball
  cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = imutils.grab_contours(cnts)
  center = None
	# only proceed if at least one contour was found
  if len(cnts) > 0:
    # find the largest contour in the mask, then use
    # it to compute the minimum enclosing circle and
    # centroid
    c = max(cnts, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    h_pos = center[1]
    if(h_pos < 160):
      print("JUMP")
      keyboard.press(Key.up)
      keyboard.release(Key.up)
      keyboard.release(Key.down)

    elif (h_pos < 320):
      print("NORMAL")
      keyboard.release(Key.down)

    else:
      print("DOWN")
      keyboard.press(Key.down)
    # print(center)q
    # only proceed if the radius meets a minimum size
    if radius > 3:
      # draw the circle and centroid on the frame,
      # then update the list of tracked points
      cv2.circle(frame, (int(x), int(y)), int(radius),
        (0, 255, 255), 2)
      cv2.circle(frame, center, 5, (0, 0, 255), -1)

    
  cv2.imshow("Color Tracker", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
        break 