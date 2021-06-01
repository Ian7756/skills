import tensorflow as tf
import cv2 as cv
import numpy as np

img = cv.imread("shu.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.resize(gray,dsize=(28,28))
gray = cv.bitwise_not(gray)/255

k = cv.waitKey(0)

resImg = np.reshape(gray,(1,28,28))

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model = tf.keras.models.load_model("fashion_model")

dict_labels = model.predict(resImg)

print(class_names[np.argmax(dict_labels)])
