import cv2 as cv

img = cv.imread("gibran.jpg")
img2 = cv.imread("bowo.png")

tinggi, lebar, _ = img.shape

#border
cv.rectangle(img, (0,0), (lebar, tinggi),(255,255,255),5)
cv.rectangle(img2, (0,0), (lebar, tinggi),(255,255,255),5)

cv.rectangle(img, (0,300), (lebar, tinggi),(255,255,255),100)
cv.rectangle(img2, (0,300), (lebar, tinggi),(255,255,255),100)

#draw text
text = "Gibran Rakabuming Raka, B.Sc"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 0.9
textcolor = (0,0,0)
thickness = thickness= 2
cv.putText(img, text,(15, tinggi-40), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "H. Prabowo Subianto"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 0.9
textcolor = (0,0,0)
thickness = thickness= 2
cv.putText(img2, text,(50, tinggi-40), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "Wakil Presiden Republik Indonesia"
font = cv.FONT_ITALIC
fontsize = 0.5
textcolor = (0,0,0)
thickness = thickness= 1
cv.putText(img, text,(15, tinggi-15), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "Presiden Republik Indonesia"
font = cv.FONT_ITALIC
fontsize = 0.5
textcolor = (0,0,0)
thickness = thickness= 1
cv.putText(img2, text,(40, tinggi-15), font,fontsize,textcolor,thickness, cv.LINE_AA)

#show
cv.imshow("image", img)
cv.imshow("image2", img2)
cv.waitKey(0)
cv.destroyAllWindows