# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:34:07 2018

@author: TE122613
tutotial open cv
https://docs.opencv.org/3.4.1/d0/d86/tutorial_py_image_arithmetics.html
#Image Addition
"""

# import libraries opencv and numpy
import cv2 as cv
import numpy as np

# read images
img1 = cv.imread('img1.jpg')
img2 = cv.imread('img2.jpg')

# add images both must have the same dimensions, otherwise you will receive error
img3 = cv.add(img1, img2)

# plot images
cv.imshow('image1', img1)
cv.imshow('image2', img2)
cv.imshow('add images', img3)
cv.waitKey() & 0xFF
cv.destroyAllWindows()
