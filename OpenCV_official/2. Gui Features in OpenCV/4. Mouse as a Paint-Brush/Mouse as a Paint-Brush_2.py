# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:22:17 2018

@author: TE122613
tutotial open cv
https://docs.opencv.org/3.4.1/dc/da5/tutorial_py_drawing_functions.html
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK: # event = left double-click
        cv.circle(img,(x,y),20,(255,0,0),-1) # definition of the circle
        
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

# cv.setMouseCallback('image', function)
cv.setMouseCallback('image',draw_circle) 
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()