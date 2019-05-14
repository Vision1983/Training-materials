# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 12:54:51 2018

@author: TE122613
tutotial open cv
https://docs.opencv.org/3.4.1/dc/da5/tutorial_py_drawing_functions.html
"""
#  To list all available events available, run the following code in Python terminal:
# import libraries opencv and numpy
import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )