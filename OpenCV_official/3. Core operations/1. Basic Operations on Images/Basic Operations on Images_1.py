# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:59:51 2018

@author: TE122613
tutotial open cv
https://docs.opencv.org/3.4.1/d3/df2/tutorial_py_basic_ops.html
"""

# import libraries opencv and numpy
import numpy as np
import cv2 as cv

# read image
img = cv.imread('FOOTBALL.jpg')

# read pixel color intensities
px = img[100, 100]
print (px)

# read blue color intensities
blue = img[100,100,0]
print (blue)

# write pixel color intensities
img[100, 100] = [255, 255, 255]
print (img[100, 100])



# accessing RED value
print (img.item(10,10,2))

# modifying RED value
img.itemset((10,10,2),100)
print(img.item(10,10,2))

# image shape
print( img.shape )

# image size
print( img.size )

# image data type
print( img.dtype )

# ROI region of interest
roi=img[230:280, 270:330]


cv.imshow('img',img)
cv.imshow('roi',roi)
cv.waitKey() & 0xFF
cv.destroyAllWindows()