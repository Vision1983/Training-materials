# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:46:04 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dc/d2e/tutorial_py_image_display.html
"""
# import openCV and numpy
import numpy as np
import cv2 as cv

# Load an image in 1=color , 0=grayscale, -1=unchanged ...
img = cv.imread('TE connectivity.jpg',0)

# show images
cv.imshow('image',img)

# waitting for any keypress
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('save.jpg',img)
    cv.destroyAllWindows()