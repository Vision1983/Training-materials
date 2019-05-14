# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:17:20 2019

@author: te122613
"""

# import libraries opencv, matplotlib and numpy
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# read image
img2 = cv.imread('bilateral1.jpg')

# blur image
bilateral = cv.bilateralFilter(img2,9,200,200)

# plot settings
plt.subplot(121),plt.imshow(bilateral),plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img2),plt.title('Original')
plt.xticks([]), plt.yticks([])
# show plots
plt.show()