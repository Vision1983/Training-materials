# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:39:59 2019
https://docs.opencv.org/3.4.1/d9/d61/tutorial_py_morphological_ops.html
@author: te122613
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('opening.png',0)
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

# plot settings
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('opening')
plt.xticks([]), plt.yticks([])
# show plots
plt.show()