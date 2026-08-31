import cv2 as cv

img = cv.imread("mon.jpg")

#take properties from this img
tinggi, lebar, _ = img.shape
print (f"info : Lebar{lebar} px, Tinggi: {tinggi} px ")

#border
cv.rectangle(img, (0,0), (lebar, tinggi),(255,0,255),5)

#draw text
text = "Bentuk Asli Melvin"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 1
textcolor = (255,255,255)
thickness = thickness= 2 #bisa taroh disini thicknessnya ataupun
cv.putText(img, text,(15, tinggi-15), font,fontsize,textcolor,thickness, cv.LINE_AA) #disini juga bisa

#save newfile 
newfilename = "newImage.png"
cv.imwrite(newfilename, img)
print(f"Image Saved as {newfilename}")

#show
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows