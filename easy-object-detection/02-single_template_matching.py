# USAGE
# python 02-single_template_matching.py --image images/coke_bottle.png --template images/coke_logo.png
# python 02-single_template_matching.py --image images/8_diamonds.png --template images/diamonds_template.png

# template matching isn’t perfect. Despite all the positives, template matching 
# quickly fails if there are factors of variation in your input images, including 
# changes to rotation, scale, viewing angle, etc.

# in template matching the orientation of the template and the image must be the same
# because the algorithm just sweep pixel by pixel
# Furthermore, the scale must be the same too

# At each (x, y)-location, a metric is calculated to represent how “good” or “bad” the 
# match is. Typically, we use the normalized correlation coefficient to determine how 
# “similar” the pixel intensities of the two patches are

# Bright locations of the result matrix R indicate the best matches, where dark regions 
# indicate there is very little correlation between the source and template images. Notice 
# how the result matrix’s brightest region appears at the coffee mug’s upper-left corner.

# If your input images contain these types of variations, you should not use template 
# matching — utilize dedicated object detectors including HOG + Linear SVM, Faster R-CNN, 
# SSDs, YOLO, etc.

# import the necessary pages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to input image where we'll apply template matching")
ap.add_argument("-t", "--template", type=str, required=True,
	help="path to template image")
args = vars(ap.parse_args())

# load the input image and template image from disk, then display
# them to  our screen
print("[INFO] loading images...")
image = cv2.imread(args["image"])
template = cv2.imread(args["template"])
cv2.imshow("Image", image)
cv2.imshow("Template", template)

# convert both the image and template to grayscale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# perform template matching
print("[INFO] performing template matching...")
result = cv2.matchTemplate(imageGray, templateGray,
	cv2.TM_CCOEFF_NORMED)
cv2.imshow("Template Matching Result", result)	

# find the min location and the max location values and positions
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

# if you want filter the errors (false positives)
if maxVal > 0.9:
	# determine the starting and ending (x, y)-coordinates of the
	# bounding box
	(startX, startY) = maxLoc
	endX = startX + template.shape[1]
	endY = startY + template.shape[0]

	# draw the bounding box on the image
	cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)