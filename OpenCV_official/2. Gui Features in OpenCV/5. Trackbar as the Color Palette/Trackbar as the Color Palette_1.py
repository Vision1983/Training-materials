# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:37:37 2018

@author: TE122613
tutotial open cv
https://docs.opencv.org/3.4.1/d9/dc8/tutorial_py_trackbar.html

Here we will create a simple application which shows the color you specify.
You have a window which shows the color and three trackbars to specify each of B,G,R colors. 
You slide the trackbar and correspondingly window color changes. 
By default, initial color will be set to Black.
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv
# def function which will update Trackbars
def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
# cv.createTrackbar('Name of the created trackbar', 'window name', value, max_value, onChange, userdata)
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()