# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:10:18 2019

@author: te122613
"""

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
img3 = cv.imread('median.png')

# blur image
median = cv.medianBlur(img3,5)

# plot settings
plt.subplot(131),plt.imshow(img3),plt.title('Nosiy image')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(median),plt.title('Median')
plt.xticks([]), plt.yticks([])
# show plots
plt.show()