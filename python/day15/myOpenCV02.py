import cv2 as cv
import numpy as np

img = cv.imread("images/green.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(2):
    for j in range(4):
        if j > 1:
            img[i][j] = [255,255,255]
        else:
            img[i][j] = [0,0,255]
print(img)

#cv.imshow("Display window", img)
cv.imwrite("images/halfred.png",img)
#k = cv.waitKey(0)