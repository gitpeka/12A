import cv2 as cv

images = cv.imread("task.png")
print(images.shape)

y_start = 350
y_end = 777

x_start = 20
x_end = 440

crop = images[x_start: x_end, y_start: y_end]

cv.imshow("croppedimages", crop)
cv.waitKey(0)
cv.destroyAllWindows()