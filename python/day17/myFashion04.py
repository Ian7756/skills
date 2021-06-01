import tensorflow as tf
import cv2 as cv
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model = tf.keras.models.load_model("fashion_model")

dict_labels = model.predict(test_images)

cnt = 0
for i in range(len(test_labels)):
    if test_labels[i] == np.argmax(dict_labels[i]):
        cnt += 1
    else:
        cv.imwrite("fashion_x/"+str(np.argmax(dict_labels[i]))+"_"+str(test_labels[i])+"_("+str(i)+").png",train_images[i])
k = cv.waitKey(0)

print(cnt/len(test_labels) * 100)
