import cv2
import numpy as np

image = cv2.imread('../../pictures/blocks.jpg')

# this is for the color red
lower_red = np.array([0, 0, 100])
upper_red = np.array([100, 32, 255])

# find the colors within the specified boundaries and apply the mask
mask = cv2.inRange(image, lower_red, upper_red)
output = cv2.bitwise_and(image, image, mask = mask)

# show the images
cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)