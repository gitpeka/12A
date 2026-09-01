import cv2 as cv

image = cv.imread("foto.jpg")
print(image.shape)

#cropping (edit nanti)
y_start = 20
y_end = 150

x_start = 15
x_end = 200

crop = image[x_start: x_end, y_start: y_end]

#effect (edit nanti)
blackwhitefilter = cv.cvtColor(crop,cv.COLOR_BGR2GRAY)

#text (edit nanti)
text = "Marcelino Dylan Ham"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.3
textcolor = (0,0,255)
thickness = thickness= 2 #bisa taroh disini thicknessnya ataupun
cv.putText(blackwhitefilter, text,(15, 165), font,fontsize,textcolor,thickness, cv.LINE_AA) #disini juga bisa

#save newfile 
newfilename = "hasil_edit.jpg"
cv.imwrite(newfilename, blackwhitefilter)
print(f"Image Saved as {newfilename}")

cv.imshow("croppedimages", blackwhitefilter)
cv.imshow("gambar",image)

cv.waitKey(0)
cv.destroyAllWindows()