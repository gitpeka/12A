import cv2 as cv

image = cv.imread("images.jpg")
blackwhitefilter = cv.cvtColor(image,cv.COLOR_BGR2GRAY)


cv.imshow('filtered',blackwhitefilter)
cv.imshow('original',image)

cv.waitKey(0)
cv.destroyAllWindows()