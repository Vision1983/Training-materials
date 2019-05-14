# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:55:52 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dc/d2e/tutorial_py_image_display.html

difference between colors order for matplotlib and opencv
"""
# import openCV, matplotlib and numpy
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
img = cv2.imread('TE connectivity.jpg')

# split color as B G R
b,g,r = cv2.split(img)

# merge color as R B G
img2 = cv2.merge([r,g,b])

# mathplotlib plot
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

# opencv plot
cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()