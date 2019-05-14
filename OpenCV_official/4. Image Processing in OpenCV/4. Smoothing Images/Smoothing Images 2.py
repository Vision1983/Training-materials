# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:44:18 2019
https://docs.opencv.org/3.4.1/d4/d13/tutorial_py_filtering.html
@author: te122613
"""
# import libraries opencv, matplotlib and numpy
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# read image
img = cv.imread('opencv_logo.png')

# blur image
blur1 = cv.blur(img,(5,5))
blur2 = cv.GaussianBlur(img,(5,5),0)


# plot settings
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(blur1),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(blur2),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
# show plots
plt.show()