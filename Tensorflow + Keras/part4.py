# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:48:32 2018

@author: te122613

open console in your virtual env and type:
tensorboard --logdir=logs/ --host localhost --port 5001

visualzation is possible to see on pages:
http://localhost:5001

https://pythonprogramming.net/tensorboard-analysis-deep-learning-python-tensorflow-keras/?completed=/convolutional-neural-network-deep-learning-python-tensorflow-keras/

základní neuronová sít, načtení předzpracovaných dat z pickle + import vizualizace Tensorboard
"""

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

NAME = "Cats-vs-dogs-cnn128-64-32-x2-{}".format(int(time.time()))

tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

"""
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess = tf.Session(config = tf.configProto(gpu_options = gpu_options))
"""
pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

X=X/255.0

model = Sequential()

model.add(Conv2D(128, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(32))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="binary_crossentropy",
              optimizer = "adam",
              metrics=['accuracy'])
model.fit(X,y, batch_size=32, epochs=10, validation_split=0.3, callbacks =[tensorboard])