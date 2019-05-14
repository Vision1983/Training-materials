# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:42:55 2018

@author: te122613

tutotial open cv
https://docs.opencv.org/3.4.1/da/d6e/tutorial_py_geometric_transformations.html
Rotation
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv

# read image
img = cv.imread('messi5.jpg',0)

# image shape
rows,cols = img.shape

# image angle and scale after transformation
angle = 90
scale = 1

# tranformation / rotation matrix cv.getRotationMatrix2D((center_X,center_Y),angle, scale)
M = cv.getRotationMatrix2D((cols/2,rows/2),angle,scale)

# image transformation cv.(image, transformation matrix, (col, row))
dst = cv.warpAffine(img,M,(cols,rows))

# plot image
cv.imshow('img',img)
cv.imshow('img trans',dst)

# close image
cv.waitKey(0)
cv.destroyAllWindows()