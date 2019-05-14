# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:50:03 2019
https://docs.opencv.org/3.4.1/d7/d4d/tutorial_py_thresholding.html
@author: te122613
"""
# import libraries opencv, matplotlib and numpy
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# read image
img = cv.imread('sudoku.jpg',0)

# blur image
img = cv.medianBlur(img,5)

# treshold image
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

# titles
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# img name
images = [img, th1, th2, th3]

#plot images
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()