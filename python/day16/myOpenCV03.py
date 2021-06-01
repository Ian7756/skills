import cv2 as cv
import numpy as np


for i in range(2):
    img = cv.imread("C:\Users\-02\바탕 화면\test_img"+"test"+i+".png")
    for j in range(4):
        if j > 1:
            img[i][j] = [255,255,255]
        else:
            img[i][j] = [0,0,255]
print(img)

#cv.imshow("Display window", img)
cv.imwrite("images/halfred.png",img)
k = cv.waitKey(0)