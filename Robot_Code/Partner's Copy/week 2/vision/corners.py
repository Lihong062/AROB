import cv2
import numpy as np

filename = '/home/marc/Pictures/chessboard.png'
image = cv2.imread(filename)

def getCorners(image):
    # Convert the image to greyscale to make all the math simpler
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # cornerHarris works best with an array of floats,
    # so that math is not rounded to the nearest integer at each step
    gray_image = np.float32(gray_image)

    # Returns a set of keypoints containing: x,y,intensity
    # Intensity means "how sure is OpenCV that this is a corner", 0-255
    corners = cv2.cornerHarris(gray_image,2,3,0.04)

    # Dilate the results to make the keypoints easier for us to see.
    corners = cv2.dilate(corners,None)
    return corners

def highlightSignificantCorners(corners, image):
    # For each corner, show it as green on the main image
    # if its intensity is at least 1% of the most intense corner.
    # Remember, intensity is how certain OpenCV is that it's a corner, 0-255. 

    # for rowIndex in range(len(corners)):
    #     for pixelIndex in range(len(corners[0])):
    #         if corners[rowIndex][pixelIndex] > (0.01 * corners.max()):
    #             image[rowIndex][pixelIndex] = [0, 255, 0]

    # This line is equivalent to the nested loop above, but much faster.
    image[corners > 0.01 * corners.max()] = [0, 255, 0] 

corners = getCorners(image)
highlightSignificantCorners(corners, image)

cv2.imshow('corners',image)
cv2.waitKey(0)