# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2 as cv
import numpy as np
import tensorflow as tf

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
  
train_labels = to_categorical(train_labels)
test_labels_shape = to_categorical(test_labels)

model = tf.keras.models.load_model("mnist_model")

dict_labels = model.predict(test_images)
cnt = 0
for i in range(len(test_labels)):
    if test_labels[i] == np.argmax(dict_labels[i]):
        cnt += 1

print(cnt/len(test_labels) * 100)

k = cv.waitKey(0)