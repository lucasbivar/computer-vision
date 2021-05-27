from ast import iter_child_nodes
import cv2
import numpy as np


FRAME_WIDTH = 480
FRAME_HEIGHT = 640
cap = cv2.VideoCapture(0)
# cap.open(URL)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

def preProcessing(img):
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
  imgCanny = cv2.Canny(imgBlur, 200, 200)
  kernel = np.ones((5,5))
  imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
  imgThres = cv2.erode(imgDial, kernel, iterations=1)
  return imgThres


def getContours(img):
  contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  maxArea = 0
  biggest = np.array([])
  for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 6000:
      peri = cv2.arcLength(cnt, True)
      approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
      objCor = len(approx)
      if area > maxArea and objCor == 4:
        biggest = approx
        maxArea = area
  cv2.drawContours(imgCountour, biggest, -1, (255,0,0),20)
  return biggest


def reorder(myPoints):
  myPoints = myPoints.reshape((4, 2))
  myPointsNew = np.zeros((4,1,2), np.int32)
  add = myPoints.sum(1)
  
  myPointsNew[0] = myPoints[np.argmin(add)]
  myPointsNew[2] = myPoints[np.argmax(add)]
  diff = np.diff(myPoints, axis=1)
  myPointsNew[1] = myPoints[np.argmin(diff)]
  myPointsNew[3] = myPoints[np.argmax(diff)]
  return myPointsNew


def getWarp(img, biggest ):
  biggest = reorder(biggest)
  pts1 = np.float32(biggest)
  pts2 = np.float32([[0,0], [FRAME_WIDTH,0], [FRAME_WIDTH,FRAME_HEIGHT], [0, FRAME_HEIGHT]])
  matrix = cv2.getPerspectiveTransform(pts1, pts2)
  imgOutput = cv2.warpPerspective(img, matrix, (FRAME_WIDTH, FRAME_HEIGHT))
  imgCropped = imgOutput[20:imgOutput.shape[0]-20, 20:imgOutput.shape[1]-20]
  imgCropped = cv2.resize(imgCropped, (FRAME_WIDTH, FRAME_HEIGHT))
  return imgCropped


while True:
  success, img = cap.read()
  img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))
  imgCountour = img.copy()

  imgThres = preProcessing(img)
  biggest = getContours(imgThres)
  if len(biggest) != 0:
    imgWarp = getWarp(img, biggest)
    cv2.imwrite("./image_scanned.png", imgWarp)
    cv2.imshow("Warped Image", imgWarp)

  cv2.imshow("Image Capture", imgCountour)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break