import cv2
import imutils

# image = cv2.imread("coins02.png")
cap = cv2.VideoCapture(0)
address = "https://192.168.15.175:8080/video"
cap.open(address)

while True:
  ret, image = cap.read()
  image = imutils.resize(image, width=800)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

  output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)
  (numLabels, labels, stats, centroids) = output

  numberOfCoins = 0
  for i in range(1, numLabels):
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    (cX, cY) = centroids[i]
    radiusH = h//2
    radiusW = w//2
    radiusABS = abs(radiusH-radiusW)
    if radiusABS < 2 and area > 1100:
      print(area)
      cv2.circle(image, (int(cX), int(cY)), radiusH, (0, 0, 255), 3)
      numberOfCoins += 1

  print(f"Number of Coins: {numberOfCoins}")
  cv2.putText(image,f"Number of Coins: {numberOfCoins}", (25, 420), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))
  cv2.imshow("Coins Counter", image)
  if cv2.waitKey(1) & 0xFF == ord('q'):
        break