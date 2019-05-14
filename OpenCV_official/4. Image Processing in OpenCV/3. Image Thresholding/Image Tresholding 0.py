# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:45:30 2019
https://docs.opencv.org/3.4.1/d7/d4d/tutorial_py_thresholding.html
@author: te122613
"""
# import libraries opencv, matplotlib and numpy
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# read image
img = cv.imread('gradient.jpg',0)

# treshold image
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

# titles
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']

# img name
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

#plot images
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()