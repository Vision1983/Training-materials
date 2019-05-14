# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:59:25 2018

@author: te122613
tutotial open cv
https://docs.opencv.org/3.4.1/df/d9d/tutorial_py_colorspaces.html
"""
# import libraries opencv and numpy
import cv2 as cv

flags =  [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

