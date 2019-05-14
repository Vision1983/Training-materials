# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 16:23:36 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dd/d43/tutorial_py_video_display.html
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(1)

w = 800
h = 600

ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,w)     # frame width
ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,h)    # frame height

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc, 10.0, (w,h))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()