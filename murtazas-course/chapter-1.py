import cv2

# the parameter of videocapture can be the webcam id or the video path
cap = cv2.VideoCapture(0)

# we can resize the video capture too
#changing the width
cap.set(3, 640)
#changing the height
cap.set(4, 480)
#changing the brightness
cap.set(10, 100)

#video is a collection of images (frames), so we have to create a loop 
# passing in each frame
while True:
  # read the frame and store in img
  # success is a boolean value indicating whether its was successful or not
  success, img = cap.read()

  #show the image
  cv2.imshow('Video', img)

  # wait press 'q' to stop
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break