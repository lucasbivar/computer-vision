# USAGE

# python 02-morphological_ops.py --image images/pyimagesearch_logo.png

# We use this operations in binary image or grayscale

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and display it to our
# screen
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# erosions are most useful for removing small blobs from an image or
# disconnecting two connected components. With this in mind, take a 
# look at the letter “p” in the PyImageSearch logo. Notice how the circular 
# region of the “p” has disconnected from the stem after 2 erosions — this 
# is an example of disconnecting two connected components of an image.


# apply a series of erosions
for i in range(0, 3):
	eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
	cv2.imshow("Eroded {} times".format(i + 1), eroded)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)





#The opposite of an erosion is a dilation. Just like an e
#rosion will eat away at the foreground pixels, a dilation 
# will grow the foreground pixels.

#Dilations increase the size of foreground objects and are 
#especially useful for joining broken parts of an image together.
# Unlike an erosion where the foreground region is slowly eaten away at, 
# a dilation actually grows our foreground region.

# Dilations are especially useful when joining broken parts of an object 
# — for example, take a look at the bottom image 
# where we have applied a dilation with 3 iterations. 
# By this point, the gaps between all letters in the logo have been joined.

# apply a series of dilations
for i in range(0, 3):
	# none =  3×3 8-neighborhood structuring element 
	dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
	cv2.imshow("Dilated {} times".format(i + 1), dilated)
	cv2.waitKey(0)

# close all windows to cleanup the screen, then initialize a list of
# of kernels sizes that will be applied to the image
cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

# Opening
# An opening is an erosion followed by a dilation.

# Performing an opening operation allows us to remove
# small blobs from an image: first an erosion is applied 
# to remove the small blobs, then a dilation is applied to 
# regrow the size of the original object.


# loop over the kernels sizes
for kernelSize in kernelSizes:
	# construct a rectangular kernel from the current size and then
	# apply an "opening" operation
	# We pass in a value of cv2.MORPH_RECT to indicate that we want a rectangular 
	# structuring element. But you could also pass in a value of cv2.MORPH_CROSS 
	# to get a cross shape structuring element (a cross is like a 4-neighborhood 
	# structuring element, but can be of any size), or cv2.MORPH_ELLIPSE to get a 
	# circular structuring element.
	# Exactly which structuring element you use is dependent upon your application 
	# — and I’ll leave it as an exercise to the reader to play with each of these 
	# structuring elements.

	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({}, {})".format(
		kernelSize[0], kernelSize[1]), opening)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# Closing
# The exact opposite to an opening would be a closing. A closing is 
# a dilation followed by an erosion.

# As the name suggests, a closing is used to close holes inside of objects or 
# for connecting components together.

# loop over the kernels sizes again
for kernelSize in kernelSizes:
	# construct a rectangular kernel form the current size, but this
	# time apply a "closing" operation
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("Closing: ({}, {})".format(
		kernelSize[0], kernelSize[1]), closing)
	cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)



# Morphological gradient

# A morphological gradient is the difference between a dilation and erosion. 
# It is useful for determining the outline of a particular object of an image:

# loop over the kernels a final time
for kernelSize in kernelSizes:
	# construct a rectangular kernel and apply a "morphological
	# gradient" operation to the image
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
	cv2.imshow("Gradient: ({}, {})".format(
		kernelSize[0], kernelSize[1]), gradient)
	cv2.waitKey(0)