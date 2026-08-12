import cv2 as cv

images = cv.imread("mango.jpg")
print(images.shape)

y_start = 70
y_end = 150

x_start = 50
x_end = 150

crop = images[x_start: x_end, y_start: y_end]

cv.imshow("croppedimages", crop)
cv.imshow("images", images)
cv.waitKey(0)
cv.destroyAllWindows()