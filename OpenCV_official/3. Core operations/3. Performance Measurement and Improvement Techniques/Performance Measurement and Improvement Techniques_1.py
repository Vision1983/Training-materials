# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:18:46 2018

@author: te122613
tutotial open cv
https://docs.opencv.org/3.4.1/dc/d71/tutorial_py_optimization.html
# Measuring Performance with OpenCV
# Default Optimization in OpenCV
"""
# import libraries opencv and numpy
import cv2 as cv
import numpy as np

# read image
img1 = cv.imread('TE connectivity.jpg')

# get counter before
e1 = cv.getTickCount()

# some image processing where we want to measure time of operation
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
    
# get counter after
e2 = cv.getTickCount()
# time is equal to counter difference divided by counter frequency
t = (e2 - e1)/cv.getTickFrequency()
print( t )

# is it opnecv optimized??
print('OpenCv is optimized = ' + str(cv.useOptimized()))