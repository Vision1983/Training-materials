# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:29:23 2018

@author: te122613

https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/
ukazkový program - jak snadno vytvořit ML s KERAS s MNIST databazi rucne psaných číslic
"""

import tensorflow as tf

print(tf.__version__)

mnist = tf.keras.datasets.mnist # 28x28 images of the hand written digits 0-9
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer= 'adam',
              loss= 'sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs = 3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print("Val_Loss ",val_loss,", Val_Acc ", val_acc)


 #save model
tf.keras.models.save_model(model,
    "epic_num_reader2.model",
    overwrite=True,
    include_optimizer=True)

 #load model
new_model=tf.keras.models.load_model('epic_num_reader2.model')
predictions = new_model.predict([x_test])
#print(predictions)

 #import
import numpy as np
import matplotlib.pyplot as plt

 #print + plot
print("Prediction of the number is "+ str(np.argmax(predictions[587])))
plt.imshow(x_test[587],cmap=plt.cm.binary)
plt.show()