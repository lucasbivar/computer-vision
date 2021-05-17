

# # USAGE
# python bilateral.py

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
	help="path to input image")
args = vars(ap.parse_args())

# load the image, display it to our screen, and construct a list of
# bilateral filtering parameters that we are going to explore
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]


# Bilateral blurring ( cv2.bilateralFilter )
# the intention of our blurring methods have been to reduce noise 
# and detail in an image; however, as a side effect we have tended to 
# lose edges in the image.
# To reduce noise while still maintaining edges, we can use bilateral blurring.
# Bilateral blurring accomplishes this by introducing two Gaussian distributions.

# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering to the image using the current set of
	# parameters
	blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)

	# show the output image and associated parameters
	title = "Blurred d={}, sc={}, ss={}".format(
		diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)