# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2 as cv
import numpy as np

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# for i in range(len(train_images)):
#     cv.imwrite("number/"+str(train_labels[i])+"_"+str(i)+".png",train_images[i])



cv.imwrite("number/pre.png",test_images[0])

# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
  
# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels_shape = to_categorical(test_labels)

# 모델 정의하기 (여기에서는 Sequential 클래스 사용)
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))
# 모델 컴파일 하기
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
# fit() 메서드로 모델 훈련 시키기
model.fit(train_images, train_labels, epochs=5, batch_size=128)
dict_labels = model.predict(test_images)

# print(test_labels[0])
# print(np.argmax(dict_labels[0]))

cnt = 0

for i in range(len(test_labels)):
    if test_labels[i] == np.argmax(dict_labels[i]):
        cnt += 1

print(cnt/len(test_labels) * 100)

k = cv.waitKey(0)