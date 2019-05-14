# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 10:54:43 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dc/d2e/tutorial_py_image_display.html
"""
# import openCV and numpy
import numpy as np
import cv2 as cv

# Load an image in 1=color , 0=grayscale, -1=unchanged ...
img_color = cv.imread('TE connectivity.jpg',1)
img_greyscale = cv.imread('TE connectivity.jpg',0)
img_unchanged = cv.imread('TE connectivity.jpg',-1)
img_abc = cv.imread('abc.jpg',-1)


# named window - define behavioral of the window
# cv.WINDOW_AUTOSIZE or cv.WINDOW_NORMAL
cv.namedWindow('img_abc', cv.WINDOW_AUTOSIZE)


# show images
cv.imshow('img_color',img_color)
cv.imshow('img_greyscale',img_greyscale)
cv.imshow('img_unchanged',img_unchanged)
cv.imshow('img_abc',img_abc)



# waitting for any keypress
# If you are using a 64-bit machine, you will have to modify k = cv.waitKey(0) line as follows cv.waitKey(0) & 0xFF
cv.waitKey(0) & 0xFF

# close all windows
cv.destroyAllWindows()
