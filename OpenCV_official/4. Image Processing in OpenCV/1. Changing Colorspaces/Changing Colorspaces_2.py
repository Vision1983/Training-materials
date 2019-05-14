# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:06:19 2018

@author: te122613
tutotial open cv
https://docs.opencv.org/3.4.1/df/d9d/tutorial_py_colorspaces.html
"""
# import libraries opencv and numpy
import cv2 as cv
import numpy as np

color_RGB = np.uint8([[[255,0,0 ]]])
color_HSV =  cv.cvtColor(color_RGB,cv.COLOR_BGR2HSV)
print(color_HSV)

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of color in HSV, actual settings is pink
    lower_color = np.array([160,150,50])
    upper_color = np.array([180,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_color, upper_color)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
