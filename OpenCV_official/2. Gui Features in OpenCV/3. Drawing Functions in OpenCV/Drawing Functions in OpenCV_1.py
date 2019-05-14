# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 10:00:56 2018

@author: TE122613

tutotial open cv
https://docs.opencv.org/3.4.1/dc/da5/tutorial_py_drawing_functions.html
"""
# import libraries opencv and numpy
import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
# cv.line(image, (start point x,y), endpoint (x,y), (color b,g,r), thickness)
cv.line(img,(0,0),(511,511),(255,0,0),5)

# cv.rectangle(image,(top left corner x,y), (bottom right corner x,y), (color b,g,r), thickness), thickness = -1 -> filled object
cv.rectangle(img,(384,0),(510,128),(0,255,0),5)

# cv.circle(image, (center x,y), radius,(color b,g,r), thickness) thickness = -1 -> filled object
cv.circle(img,(447,63), 63, (0,0,255), -1)

#cv.ellipse(imgage, (center x,y), (axes lenght x,y), rotation, startAngle, endAngle, (color b,g,r), thickness) thickness = -1 -> filled object
cv.ellipse(img,(256,256),(100,50),0,0,360,(0,255,0),3)

# in numpz create arraz of points
pts = np.array([[20,5],[20,30],[70,20],[50,10], [50,5] ], np.int32)
#  reshape array, reshape(array to be reshaped, new shape, order)
pts = pts.reshape((-1,1,2))
# cv.polylines(image, [pts =points of polygon [x,y]], is closed? T/F,(color b,g,r), thickness) thickness > -1
cv.polylines(img,[pts],True,(0,255,255),5)

# font selection
font = cv.FONT_HERSHEY_SIMPLEX

# cv.putText(image, 'text to be plotted', position, font,font scale,(color b,g,r), thickness, line type, bottomLeftOrigin T/F  )
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA, False)

# plot image
cv.imshow('img',img)

# waitting for any keypress
# If you are using a 64-bit machine, you will have to modify k = cv.waitKey(0) line as follows cv.waitKey(0) & 0xFF
cv.waitKey(0) & 0xFF

# close all windows
cv.destroyAllWindows()
