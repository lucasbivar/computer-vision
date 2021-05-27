# FACE DETECTION
import cv2

faceCascade = cv2.CascadeClassifier("murtazas-course/resources/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
  # img = cv2.imread('murtazas-course/resources/lena.jpg')
  success, img = cap.read()
  imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

  for face in faces:
    (x, y, w, h) = face
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0,0), 2)

  cv2.imshow("Face Detection", img)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break