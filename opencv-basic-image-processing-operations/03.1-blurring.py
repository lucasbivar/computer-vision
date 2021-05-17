# While this effect is usually unwanted in our photographs, it’s actually quite 
# helpful when performing image processing tasks. In fact, smoothing and blurring
# is one of the most common preprocessing steps in computer vision
# and image processing.

# For example, we can see that blurring is applied when building a simple
# document scanner on the PyImageSearch blog. We also apply smoothing to aid 
# us in finding our marker when measuring the distance from an object to our camera. 
# In both these examples the smaller details in the image are smoothed out and we are 
# left with more of the structural aspects of the image

# Smoothing and blurring is one of the most important preprocessing steps in all 
# of computer vision and image processing. By smoothing an image prior to applying
# techniques such as edge detection or thresholding we are able to reduce the 
# amount of high-frequency content, such as noise and edges (i.e., the “detail”
#  of an image).

# While this may sound counter-intuitive, by reducing the detail in an 
# image we can more easily find objects that we are interested in.

# Furthermore, this allows us to focus on the larger structural objects in the image.


# USAGE
# python blurring.py

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
	help="path to input image")
args = vars(ap.parse_args())

# load the image, display it to our screen, and initialize a list of
# kernel sizes (so we can evaluate the relationship between kernel
# size and amount of blurring)
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

# Average blurring ( cv2.blur )
# An average filter does exactly what you think it might do — 
# takes an area of pixels surrounding a central pixel, averages all 
# these pixels together, and replaces the central pixel with the average.

# By taking the average of the region surrounding a pixel, we are smoothing 
# it and replacing it with the value of its local neighborhood. This allows 
# us to reduce noise and the level of detail, simply by relying on the average.

# loop over the kernel sizes
for (kX, kY) in kernelSizes:
	# apply an "average" blur to the image using the current kernel
	# size
	blurred = cv2.blur(image, (kX, kY))
	cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)


# Gaussian blurring ( cv2.GaussianBlur)
# Gaussian blurring is similar to average blurring, but instead 
# of using a simple mean, we are now using a weighted mean, where 
# neighborhood pixels that are closer to the central pixel contribute 
# more “weight” to the average.

# And as the name suggests, Gaussian smoothing is used to remove noise 
# that approximately follows a Gaussian distribution.

# The end result is that our image is less blurred, but more “naturally blurred

# loop over the kernel sizes again
for (kX, kY) in kernelSizes:
	# apply a "Gaussian" blur to the image
	blurred = cv2.GaussianBlur(image, (kX, kY), 0)
	cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# Median blurring ( cv2.medianBlur )
# the median blur method has been most effective when removing 
# salt-and-pepper noise. This type of noise is exactly what it 
# sounds like: imagine taking a photograph, putting it on your dining 
# room table, and sprinkling salt and pepper on top of it. Using the 
# median blur method, you could remove the salt and pepper from your image.

# loop over the kernel sizes a final time
for k in (3, 9, 15):
	# apply a "median" blur to the image
	blurred = cv2.medianBlur(image, k)
	cv2.imshow("Median {}".format(k), blurred)
	cv2.waitKey(0)