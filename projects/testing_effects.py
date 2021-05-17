import numpy as np
import imutils
import cv2
from numpy.core.fromnumeric import shape
def nothing(arg):
  pass

cv2.namedWindow('frame')
cv2.createTrackbar("Brightness", "frame" , 0, 255, nothing)
cv2.createTrackbar("Darkness", "frame" , 0, 255, nothing)

cv2.createTrackbar("Red-high", "frame" , 0, 255, nothing)
cv2.createTrackbar("Red-low", "frame" , 0, 255, nothing)

cv2.createTrackbar("Green-high", "frame" , 0, 255, nothing)
cv2.createTrackbar("Green-low", "frame" , 0, 255, nothing)

cv2.createTrackbar("Blue-high", "frame" , 0, 255, nothing)
cv2.createTrackbar("Blue-low", "frame" , 0, 255, nothing)

cv2.createTrackbar("Resize", "frame" , 0, 50, nothing)

cv2.createTrackbar("Sharpness", "frame" , 0, 1, nothing)
cv2.createTrackbar("Blur", "frame" , 0, 25, nothing)



cap = cv2.VideoCapture(0)

sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    (h, w) = frame.shape[:2]
    (cX, cY) = (w//2, h//2)
    
    bright = int(cv2.getTrackbarPos('Brightness',"frame"))
    dark = int(cv2.getTrackbarPos('Darkness',"frame"))

    M = np.ones(frame.shape, dtype="uint8") * bright
    frame = cv2.add(frame, M)
    M = np.ones(frame.shape, dtype="uint8") * dark
    frame = cv2.subtract(frame, M)

    red_high = int(cv2.getTrackbarPos("Red-high", "frame"))
    green_high = int(cv2.getTrackbarPos("Green-high", "frame"))
    blue_high = int(cv2.getTrackbarPos("Blue-high", "frame"))

    red_low = int(cv2.getTrackbarPos("Red-low", "frame"))
    green_low = int(cv2.getTrackbarPos("Green-low", "frame"))
    blue_low = int(cv2.getTrackbarPos("Blue-low", "frame"))

    (B, G, R) = cv2.split(frame)

    M = np.ones(R.shape, dtype="uint8") * red_high
    R = cv2.add(R, M)
    M = np.ones(R.shape, dtype="uint8") * red_low
    R = cv2.subtract(R, M)

    M = np.ones(G.shape, dtype="uint8") * green_high
    G = cv2.add(G, M)
    M = np.ones(G.shape, dtype="uint8") * green_low
    G = cv2.subtract(G, M)

    M = np.ones(B.shape, dtype="uint8") * blue_high
    B = cv2.add(B, M)
    M = np.ones(B.shape, dtype="uint8") * blue_low
    B = cv2.subtract(B, M)

    frame = cv2.merge([B, G, R])
    
    new_size = int(cv2.getTrackbarPos("Resize", "frame"))
    frame = imutils.resize(frame, width=(w + (w*new_size)//100))

    # cv2.rectangle(frame,(cX-100, cY-100),(cX+100,cY+100), (0, 0, 255), 2)
    # cv2.circle(frame, (cX, cY), 110, (0, 0, 255), 2)

    blur_factor = int(cv2.getTrackbarPos("Blur", "frame"))
    if blur_factor > 0:
      smallBlur = np.ones((blur_factor, blur_factor), dtype="float") * (1.0 / (blur_factor * blur_factor))
      frame = cv2.filter2D(frame, -1, smallBlur)
    
    sharpness = int(cv2.getTrackbarPos("Sharpness", "frame"))
    if(sharpness == 1):
      frame = cv2.filter2D(frame, -1, sharpen)
    


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()