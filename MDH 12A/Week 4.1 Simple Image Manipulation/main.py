import cv2 as cv

image = cv.imread("pommy.jpg")
blackwhitefilter = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
gaussianblur = cv.GaussianBlur(image, (5,5), 0)

gaussianblackwhitefilter =  cv.GaussianBlur(blackwhitefilter, (5,5), 0)

cv.imshow("original",image)
cv.imshow('filtered',blackwhitefilter)
cv.imshow('filteredgaubw',gaussianblackwhitefilter)

cv.waitKey(0)
cv.destroyAllWindows()