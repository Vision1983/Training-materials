# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:28:54 2018

@author: te122613

tutotial open cv
https://docs.opencv.org/3.4.1/da/d6e/tutorial_py_geometric_transformations.html
Translation
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv

# read image
img = cv.imread('messi5.jpg',0)
# image shape
rows,cols = img.shape

# translation location tx, ty
tx = 100
ty = 50

# translation matrix
M = np.float32([[1,0,tx],[0,1,ty]])

# image transformation cv.(image, transformation matrix, (col, row))
dst = cv.warpAffine(img,M,(cols,rows))

# plot image
cv.imshow('img',img)
cv.imshow('img trans',dst)

# close image
cv.waitKey(0)
cv.destroyAllWindows()