# USAGE
# python 02-morphological_hats.py --image images/car.png

# We can use this operations with not binary images too

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# A top hat (also known as a white hat) morphological operation is 
# the difference between the original (grayscale/single channel) input
# image and the opening.

# A top hat operation is used to reveal bright regions of an image on 
# dark backgrounds.

# Up until this point we have only applied morphological operations to
# binary images. But we can also apply morphological operations to grayscale
# images as well. In fact, both the top hat/white hat and the black hat operators
# are more suited for grayscale images rather than binary ones.


# construct a rectangular kernel (13x5) and apply a blackhat
# operation which enables us to find dark regions on a light
# background

# rectangular structuring element with a width of 13 pixels and a height 
# of 5 pixels. As I mentioned earlier in this lesson, structuring elements 
# can be of arbitrary size. And in this case, we are applying a rectangular 
# element that is almost 3x wider than it is tall.
# And why is this?
# Because a license plate is roughly 3x wider than it is tall!
# By having some basic a priori knowledge of the objects you want to detect
# in images, we can construct structuring elements to better aid us in finding them
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# similarly, a tophat (also called a "whitehat") operation will
# enable us to find light regions on a dark background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# show the output images
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)