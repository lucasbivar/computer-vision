import cv2
import cv2
import numpy as np


FRAME_WIDTH = 640
FRAME_HEIGHT = 480
MIN_AREA = 500
cap = cv2.VideoCapture(0)
# cap.open(URL)
cap.set(3, FRAME_WIDTH)
cap.set(4, FRAME_HEIGHT)
cap.set(10, 150)


plateCascade = cv2.CascadeClassifier("projects/resources/haarcascade_license_plate_rus_16stages.xml")

count = 0
while True:
  # success, img = cap.read()
  img = cv2.imread('projects/resources/license_plate.jpg')
  img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))

  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  plates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

  for plate in plates:
    (x, y, w, h) = plate
    if w*h > MIN_AREA:
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0,0), 2)
      cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0))
      imgRoi = img[y:y+h, x:x+w]
      cv2.imshow("ROI", imgRoi)

  cv2.imshow("Image", img)

  if cv2.waitKey(1) & 0xFF == ord('s'):
    count += 1
    cv2.imwrite("projects/resources/NoPlate_"+str(count)+".jpg", imgRoi)
    cv2.rectangle(img, (0,200), (640, 300), (0, 255,0), cv2.FILLED)
    cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (0,0,255),2)
    cv2.imshow("Image", img)
    cv2.waitKey(500)
    
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break