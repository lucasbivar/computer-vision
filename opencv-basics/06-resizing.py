import cv2
import argparse
import imutils
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/guitar.jpg", help="path to input image")
args = vars(ap.parse_args())

#Implementing basic image resizing with OpenCV

# load the original input image and display it to our screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# let's resize our image to be 150 pixels wide, but in order to
# prevent our resized image from being skewed/distorted, we must
# first calculate the ratio of the *new* width to the *old* width
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)


# let's resize the image to have a width of 50 pixels, again keeping
# in mind the aspect ratio
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)


# calculating the ratio each and every time we want to resize an
# image is a real pain, so let's use the imutils convenience
# function which will *automatically* maintain our aspect ratio
# for us
resized = imutils.resize(image, width=100)
# we can specify the height instead width too
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)


#COMPARING OPENCV INTERPOLATION METHODS

# construct the list of interpolation methods in OpenCV
methods = [
  # big size to small size
	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),#highest quality results at a modest computation cost
	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),#better to big size to small size
	("cv2.INTER_AREA", cv2.INTER_AREA),
  # small size to big size
	("cv2.INTER_CUBIC", cv2.INTER_CUBIC), #better to small size to big size
	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

# loop over the interpolation methods
for (name, method) in methods:
	# increase the size of the image by 3x using the current
	# interpolation method
	print("[INFO] {}".format(name))
	resized = imutils.resize(image, width=image.shape[1] * 3,
		inter=method)
	cv2.imshow("Method: {}".format(name), resized);cv2.waitKey(0)

# we resize the image, because depeding of the operation, a big image can spend more time