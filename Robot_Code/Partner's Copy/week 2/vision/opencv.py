import cv2
import numpy

color_img = cv2.imread('pictures/blocks.jpg')
grayscale_img = cv2.imread('pictures/blocks.jpg',
    cv2.IMREAD_GRAYSCALE)
# print grayscale_img.shape

cv2.imshow("My awesome image in gray!", grayscale_img)
cv2.waitKey(0)

black = [0,   0,   0]
white = [255, 255, 255]
red =   [0,   0,   255]
green = [0,   255, 0]
blue =  [255, 0,   0]
decimal_number = int('A7', 16)

num_rows_in_image = len(color_img)
for row_index in range(num_rows_in_image):
    num_pixels_in_row = len(color_img[row_index])
    for pixel_index in range(num_pixels_in_row):
        # Read blue value from pixel
        blue_value = color_img[row_index][pixel_index][0]
        # Set amount of blue in pixel
        color_img[row_index][pixel_index][0] = 255
        # Set pixel BGR values to 0,0,0 - black
        color_img[row_index][pixel_index] = [0,0,0]

for row in color_img:
    for pixel in row:
        pixel = [0,0,0]
        blue_value = pixel[0]
        green_value = pixel[1]
        red_value = pixel[2]
