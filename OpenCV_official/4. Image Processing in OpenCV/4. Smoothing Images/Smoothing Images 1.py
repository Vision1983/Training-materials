# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 09:46:35 2019
https://docs.opencv.org/3.4.1/d4/d13/tutorial_py_filtering.html
@author: te122613
"""
# import libraries opencv, matplotlib and numpy
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# read image
img = cv.imread('opencv_logo.png')
#  definition of 5x5 averaging filter kernel
kernel = np.ones((5,5),np.float32)/25
# image filter with 2D Convolution
dst = cv.filter2D(img,-1,kernel)
# plot settings
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
# show plots
plt.show()