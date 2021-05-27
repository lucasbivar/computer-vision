import cv2
import numpy as np

# FRAME_HEIGHT = 480
# FRAME_WIDTH = 640

cap = cv2.VideoCapture(0)
# cap.set(3, FRAME_WIDTH)
# cap.set(4, FRAME_HEIGHT)
# cap.set(10, 150)

myColors = [[11, 51, 84, 255, 156, 255], 
[49, 88, 60, 197, 98, 157], [109, 150, 32, 136, 62, 176]]

myColorValues = [[0, 255, 255], [0, 252, 60], [250, 9, 156]]

myPoints = [] # [x, y, colorID]

def getContours(img):
  contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  x, y, w, h = 0, 0, 0, 0 
  for cnt in contours:
    area = cv2.contourArea(cnt)
    #removing noises
    if area > 500:
      # cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
      peri = cv2.arcLength(cnt, True)
      approx = cv2.approxPolyDP(cnt, 0.02*peri, True)

      x, y, w, h = cv2.boundingRect(approx)
  return x+w//2, y
     
def findColor(img, myColors, myColorValues):
  imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  count = 0
  newPoints = []
  for color in myColors:
    lower = np.array(color[0:6:2])
    upper = np.array(color[1:6:2])
    mask = cv2.inRange(imgHSV, lower, upper)
    x, y = getContours(mask)
    if x != 0 and y != 0:
      newPoints.append([x, y, count])
    count += 1
    # cv2.imshow(str(color), mask)
  return newPoints


def drawOnCanvas(myPoints, myColorValues):
  for point in myPoints:
    cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
  success, img = cap.read()
  imgResult = img.copy()
  newPoints = findColor(img, myColors, myColorValues)
  if len(newPoints) != 0:
    myPoints += newPoints
  if len(myPoints) != 0:
    drawOnCanvas(myPoints, myColorValues )
  cv2.imshow("Result", imgResult)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break