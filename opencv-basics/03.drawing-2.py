import cv2
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/guitar.jpg", help="path to input image")
args = vars(ap.parse_args())


# load the input image from disk
image = cv2.imread(args["image"])

# draw a circle around my face, two filled in circles covering my
# eyes, and a rectangle over top of my mouth
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

# show the output image
cv2.imshow("Output", image)

cv2.waitKey(0)
