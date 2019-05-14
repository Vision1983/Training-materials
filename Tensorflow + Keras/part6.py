# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 00:05:29 2018
64x3-cnn.model
@author: TE122613

predikce na základě modelu
"""


import cv2
import tensorflow as tf


categories = ["Dog","Cat"]
image = 'images.jpg'

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("64x3-cnn.model")
prediction = model.predict([prepare(image)])
print(categories[int(prediction[0][0])])

img = cv2.imread(image)
cv2.imshow('Image_Window_click ESC to close', img)
cv2.waitKey()
cv2.destroyAllWindows()