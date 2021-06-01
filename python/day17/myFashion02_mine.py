import tensorflow as tf
import numpy as np
import cv2 as cv

# 1. Fashion MNIST 데이터셋 임포트
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

for i in range(len(train_images)):
    cv.imwrite("fashion/"+str(train_labels[i])+"_"+str(i)+".png",train_images[i])


#cv.imwrite("fashion/pre.png",test_images[0])

# 2. 데이터 전처리
train_images, test_images = train_images / 255.0, test_images / 255.0

# 3. 모델 구성
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# 4. 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 5. 모델 훈련
model.fit(train_images, train_labels, epochs=5)


# 6. 정확도 평가하기
loss, accuracy = model.evaluate(test_images, test_labels)
print(loss, accuracy)

# 7. 예측하기
dict_labels = model.predict(test_images)

cnt = 0

for i in range(len(test_labels)):
    if test_labels[i] == np.argmax(dict_labels[i]):
        cnt += 1

print(cnt/len(test_labels) * 100)

k = cv.waitKey(0)