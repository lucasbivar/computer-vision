# TEXT AND SHAPES
import cv2
import numpy as np

imgGrayScale = np.zeros((512, 512))
print(imgGrayScale.shape) # (512, 512)-> grayscale image
# cv2.imshow("Image", imgGrayScale)

# creating a black image with 3 channels
img = np.zeros((512, 512, 3), np.uint8)

# fill this area with blue color (BGR - 255, 0, 0)
# img[200:300] = 255, 0, 0

# creating a line in image (image, start, end, color, thickness)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)


# creating a rectangle (image, upper left corner, bottom right corner, color, thickness or cv.FILLED)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

# creating a circle (image, center, radius, color, thickness or cv2.FILLED)
cv2.circle(img, (400, 50), 30, (255, 255 ,0), 5)

# put text (image, text, start, font, scale, color, thickness)
cv2.putText(img, " OPENCV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0),1)

cv2.imshow("Image", img)



cv2.waitKey(0)