import numpy as np
import cv2

FILENAME = 'block_challenge_3.jpg'

def find_center_of_color_blob(mask):
    # TODO: write code here
    return (average_x, average_y)

def find_corners(gray_image):
    # TODO: write code here
    return corners

def find_edges(gray_image):
    # TODO: write code here
    return blurred_edges

def highlight_center(center, image):
    """Make a single point white, to represent the center of a blob."""
    image[center[0], center[1]] = [255, 255, 255]

def highlight_edges(edges, image):
    """If this pixel is part of an edge, make it blue"""
    image[edges>0.01] = [255, 0, 0]

def highlight_significant_corners(corners, image):
    """If corner intensity is above a certain threshold, make it green"""

    # This line is equivalent to the nested loop below, but much faster.
    image[corners > 0.01 * corners.max()] = [0, 255, 0]

    # for rowIndex in range(len(corners)):
    #     for pixelIndex in range(len(corners[0])):
    #         if corners[rowIndex][pixelIndex] > (0.01 * corners.max()):
    #             image[rowIndex][pixelIndex] = [0, 255, 0]
