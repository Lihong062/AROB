import cv2
import numpy as np

image = cv2.imread('../../pictures/blocks.jpg')

lower_red = [0, 0, 100]
upper_red = [100, 32, 255]

# Check if each of a pixel's BGR values fall within a given range
# All parameters should be given as [b, g, r] arrays.
def pixel_in_range(pixel_bgr, range_min, range_max):
    blue_in_range = pixel_bgr[0] >= range_min[0] and pixel_bgr[0] <= range_max[0]
    green_in_range = pixel_bgr[1] >= range_min[1] and pixel_bgr[1] <= range_max[1]
    red_in_range = pixel_bgr[2] >= range_min[2] and pixel_bgr[2] <= range_max[2]
    return blue_in_range and green_in_range and red_in_range

output = np.copy(image) # Make a copy

for row_index in range(len(output)):
    row = output[row_index]
    for pixel_index in range(len(row)):
        pixel = row[pixel_index]
        if not pixel_in_range(pixel, lower_red, upper_red):
            pixel[0] = 0
            pixel[1] = 0
            pixel[2] = 0

# show the images
cv2.imshow("images", np.hstack([image, output]))
cv2.waitKey(0)