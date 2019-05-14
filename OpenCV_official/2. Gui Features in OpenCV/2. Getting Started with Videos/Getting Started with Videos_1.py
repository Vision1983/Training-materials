# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:21:51 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dd/d43/tutorial_py_video_display.html
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv

# set video-capture settings
port = 1  
cap = cv.VideoCapture(port)                     #port number define device
ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,800)     # frame width
ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,600)    # frame height
 
# get video-capture settings
W = cap.get(cv.CAP_PROP_FRAME_WIDTH)            # frame width
H = cap.get(cv.CAP_PROP_FRAME_HEIGHT)           # frame height

# print video settings
chip = ('Camera width ' + str(W) + ' and height '+ str(H) + ' Port ' + str(port))
print(chip)

# cycle for image acquistion, to stop cycle press q
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here, 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow(chip ,gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()