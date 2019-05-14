# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:50:11 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dc/d2e/tutorial_py_image_display.html
"""
# import openCV, matplotlib and numpy
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load an image in 1=color , 0=grayscale, -1=unchanged ...
img = cv.imread('TE connectivity.jpg',1)

# plot image
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()