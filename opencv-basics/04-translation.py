import argparse
import cv2
import imutils
import numpy as np
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", type=str, default="images/guitar.jpg", help="path to input image")
args = vars(ap.parse_args())

# load the image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# NOTE: Translating (shifting) an image is given by a NumPy matrix
# in the form:
# [
#   [1, 0, shiftX],
#   [0, 1, shiftY],
# ]
# You simply need to specify how many pixels you want to shift the image
# in the X and Y directions

# shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)


# now, let's shift the image 50 pixels to the left and 90 pixels
# up by specifying negative values for the x and y directions,
# respectively
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)


# use the imutils helper function to translate the image 100 pixels
# down in a single function call
shifted = imutils.translate(image, 0, -100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)