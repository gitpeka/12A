#alias supaya mempermudah pemanggilan library OpenCV
import cv2 as cv

image = cv.imread("pommy.jpg")
cv.imshow("tampil gambar",image)
#cv alias dari lib, imshow module, image parameter

cv.waitKey(0)
cv.destroyAllWindows()
