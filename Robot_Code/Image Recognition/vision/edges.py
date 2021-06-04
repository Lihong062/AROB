import cv2
import numpy as np

# Load the image
image = cv2.imread('/home/marc/Pictures/blocks.jpg')
# Convert the image to greyscale to make the math easier
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Blur using a 3x3 blur mask, like we talked about in class
blurred = cv2.GaussianBlur(gray_image, (3, 3), 0)

# Run edge detection on the original image
edges = cv2.Canny(image, 100, 200)
# Run edge detection on the blurred image
blurred_edges = cv2.Canny(blurred, 100, 200)
# Arguments #2 and #3 have to do with how the detection joins edges,
# and 100 and 200 are the industry standard values

# Show the images
cv2.imshow("edge detection on blurred image", blurred_edges)
cv2.imshow("edge detection on original image", edges)
cv2.waitKey(0)