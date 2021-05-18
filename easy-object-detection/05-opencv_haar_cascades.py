# USAGE
# python 05-opencv_haar_cascades.py --cascades cascades

# Haar cascades, first introduced by Viola and Jones in their seminal 2001 
# publication, Rapid Object Detection using a Boosted Cascade of Simple Features, 
# are arguably OpenCV’s most popular object detection algorithm.

# Sure, many algorithms are more accurate than Haar cascades (HOG + Linear SVM, 
# SSDs, Faster R-CNN, YOLO, to name a few), but they are still relevant and 
# useful today.

# One of the primary benefits of Haar cascades is that they are just so fast 
# — it’s hard to beat their speed.

# The downside to Haar cascades is that they tend to be prone to false-positive 
# detections, require parameter tuning when being applied for inference/detection, 
# and just, in general, are not as accurate as the more “modern” algorithms we have today.

# That said, Haar cascades are:
# 	- An important part of the computer vision and image processing literature
# 	- Still used with OpenCV
# 	- Still useful, particularly when working in resource-constrained devices 
# 		when we cannot afford to use more computationally expensive object detectors

# Problems and limitations of Haar cascades
# - However, it’s not all good news. The detector tends to be the most effective
# 	for frontal images of the face.
# - Haar cascades are notoriously prone to false-positives — the Viola-Jones 
# 	algorithm can easily report a face in an image when no face is present.
#	- It can be quite tedious to tune the OpenCV detection parameters. There will 
# 	be times when we can detect all the faces in an image. There will be other 
# 	times when (1) regions of an image are falsely classified as faces, and/or 
# 	(2) faces are missed entirely.



# import the necessary packages
import argparse
import imutils
import time
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascades", type=str, default="/home/lucas/Documents/all/computer-vision/easy-object-detection/cascades",
	help="path to input directory containing haar cascades")
args = vars(ap.parse_args())

# initialize a dictionary that maps the name of the haar cascades to
# their filenames
detectorPaths = {
	"face": "haarcascade_frontalface_default.xml",
	"eyes": "haarcascade_eye.xml",
	"smile": "haarcascade_smile.xml",
}

# initialize a dictionary to store our haar cascade detectors
print("[INFO] loading haar cascades...")
detectors = {}

# loop over our detector paths
for (name, path) in detectorPaths.items():
	# load the haar cascade from disk and store it in the detectors
	# dictionary
	path = os.path.sep.join([args["cascades"], path])
	print(path, name)
	detectors[name] = cv2.CascadeClassifier(path)
print(detectors)
# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
cap = cv2.VideoCapture(0)
time.sleep(2.0)
print(detectors["face"].empty())
# loop over the frames from the video stream
while True:
	# grab the frame from the video stream, resize it, and convert it
	# to grayscale
	ret, frame = cap.read()
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# perform face detection using the appropriate haar cascade
	faceRects = detectors["face"].detectMultiScale(
		gray, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

	# loop over the face bounding boxes
	for (fX, fY, fW, fH) in faceRects:
		# extract the face ROI
		faceROI = gray[fY:fY+ fH, fX:fX + fW]

		# apply eyes detection to the face ROI
		eyeRects = detectors["eyes"].detectMultiScale(
			faceROI, scaleFactor=1.1, minNeighbors=10,
			minSize=(15, 15), flags=cv2.CASCADE_SCALE_IMAGE)

		# apply smile detection to the face ROI
		smileRects = detectors["smile"].detectMultiScale(
			faceROI, scaleFactor=1.1, minNeighbors=10,
			minSize=(15, 15), flags=cv2.CASCADE_SCALE_IMAGE)

		# loop over the eye bounding boxes
		for (eX, eY, eW, eH) in eyeRects:
			# draw the eye bounding box
			ptA = (fX + eX, fY + eY)
			ptB = (fX + eX + eW, fY + eY + eH)
			cv2.rectangle(frame, ptA, ptB, (0, 0, 255), 2)

		# loop over the smile bounding boxes
		for (sX, sY, sW, sH) in smileRects:
			# draw the smile bounding box
			ptA = (fX + sX, fY + sY)
			ptB = (fX + sX + sW, fY + sY + sH)
			cv2.rectangle(frame, ptA, ptB, (255, 0, 0), 2)

		# draw the face bounding box on the frame
		cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH),
			(0, 255, 0), 2)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()