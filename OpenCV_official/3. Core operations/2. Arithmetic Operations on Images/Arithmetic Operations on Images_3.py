# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:01:32 2018

@author: TE122613
tutotial open cv
https://docs.opencv.org/3.4.1/d0/d86/tutorial_py_image_arithmetics.html
# Bitwise Operations
"""

# import libraries opencv and numpy
import cv2 as cv
import numpy as np

# Load two images
img1 = cv.imread('TE connectivity.jpg')
img2 = cv.imread('logo.jpg')

# logo position, shift position to coresponding area of interest
X = 650
Y = 750

# shape of the logo row, col, X,Y are position of the logo
rows,cols,channels = img2.shape
roi = img1[X:rows+X, Y:cols+Y ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)                      #filter image color to grayscale
ret, mask = cv.threshold(img2gray, 100, 255, cv.THRESH_BINARY)      #treshold image, create mask, try different intensities
mask_inv = cv.bitwise_not(mask)                                     #inverted masking

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)                   # masking foreground
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)                     # masking background
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)                                       # add images foreground and background
img1[X:rows+X, Y:cols+Y ] = dst                                     # modify img1 in ROI

# show images
cv.imshow('bg',img1_bg)
cv.imshow('fg',img2_fg)
cv.imshow('mask',mask)
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()