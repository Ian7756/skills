import cv2 as cv

img = cv.imread("images/green.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(img)

cv.imshow("Display window", img)
k = cv.waitKey(0)
