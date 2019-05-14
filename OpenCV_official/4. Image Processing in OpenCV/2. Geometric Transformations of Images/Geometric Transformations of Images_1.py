# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:30:55 2018

@author: te122613

tutotial open cv
https://docs.opencv.org/3.4.1/da/d6e/tutorial_py_geometric_transformations.html
Scaling
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv

# read image
img = cv.imread('messi5.jpg')

# resize image
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

# plot image
cv.imshow('1',img)
cv.imshow('2',res)

# close image
cv.waitKey(0)
cv.destroyAllWindows()

'''
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
'''