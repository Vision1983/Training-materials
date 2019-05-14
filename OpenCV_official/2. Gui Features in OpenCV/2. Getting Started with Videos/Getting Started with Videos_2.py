# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:09:57 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dd/d43/tutorial_py_video_display.html
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv

cap = cv.VideoCapture('TE Connectivity.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()