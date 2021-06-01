import cv2 as cv


img = cv.imread("bagi.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = cv.resize(gray,dsize=(28,28))
k = cv.waitKey(0)

