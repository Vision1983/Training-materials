# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 09:36:51 2018

@author: TE122613
tutotial open cv
https://docs.opencv.org/3.4.1/d3/df2/tutorial_py_basic_ops.html
"""

# import libraries opencv and numpy
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# definition of the color
BLUE = [0,0,255]

# read image
img1 = cv.imread('opencv.jpg')

# split and merge image - change due to BGR and RBG convention of plotting, cv2 vs matplotlib
b,g,r = cv.split(img1)
img1 = cv.merge([r,g,b])

# Making Borders for Images (Padding)
# cv.copyMakeBorder(image, top, bottim, left, right, border type)
replicate = cv.copyMakeBorder(img1,100,100,100,100,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,100,100,100,100,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,100,100,100,100,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,100,100,100,100,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,100,100,100,100,cv.BORDER_CONSTANT,value=BLUE)

# images subplot
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
