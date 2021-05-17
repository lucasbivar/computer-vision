# The gradient magnitude and orientation allow us to reveal the structure 
# of objects in an image.

# However, for the process of edge detection, the gradient magnitude is extremely 
# sensitive to noise.

# We had just the outline, we could extract the pills from the image using 
# something like contour detection. Wouldn’t that be nice?

# Unfortunately, simple image gradients are not going to allow us to (easily) 
# achieve our goal.

# Instead, we’ll have to use the image gradients as building blocks to create 
# a more robust method to detect edges — the Canny edge detector

# The Canny edge detector is a multi-step algorithm used to detect a wide range 
# of edges in images. The algorithm itself was introduced by John F. Canny in his 
# 1986 paper, A Computational Approach to Edge Detection.

# USAGE
# python opencv_canny.py --image images/coins.png

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])

# While Canny edge detection can be applied to an RGB image by detecting 
# edges in each of the separate Red, Green, and Blue channels separately 
# and combining the results back together, we almost always want to apply 
# edge detection to a single channel, grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# the blue remove the focus in details, we make this beacuse
# we want detect just the edges
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# show the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

# compute a "wide", "mid-range", and "tight" threshold for the edges
# using the Canny edge detector
# the bottom and top threshold have to be tunning manually, this 3 values
# it's a good start to tunning
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

# show the output Canny edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.waitKey(0)

# How do we choose optimal Canny edge detection parameters?
# As you can tell, depending on your input image you’ll need dramatically 
# different hysteresis threshold values — and tuning these values can be a 
# real pain. You might be wondering, is there a way to reliably tune these 
# parameters without simply guessing, checking, and viewing the results?