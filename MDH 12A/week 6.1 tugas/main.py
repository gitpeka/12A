import cv2 as cv

img = cv.imread("white.png")

tinggi, lebar, _ = img.shape #600 800

#shape
cv.rectangle(img, (50,50), (550, 750),(0,0,255),-1)
cv.circle(img, (300,1000), (800),(128,0,0),-1)
cv.rectangle(img, (0,0), (600,800),(255,255,255),97)


#draw text
text = "PERATURAN / TATA TERTIB"
font = cv.FONT_HERSHEY_DUPLEX
fontsize = 0.9
textcolor = (0,255,255)
thickness = thickness= 2
cv.putText(img, text,(125, 120), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "LABORATORIUM"
font = cv.FONT_HERSHEY_DUPLEX
fontsize = 0.9
textcolor = (0,255,255)
thickness = thickness= 2
cv.putText(img, text,(200, 145), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "KOMPUTER & BAHASA"
font = cv.FONT_HERSHEY_DUPLEX
fontsize = 0.9
textcolor = (0,255,255)
thickness = thickness= 2
cv.putText(img, text,(160, 170), font,fontsize,textcolor,thickness, cv.LINE_AA)



text = "1. Mengenakan pakaian yang rapi dan sopan"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 275), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "2. Tidak diperkenankan membawa makanan"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 295), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "dan minuman"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 315), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "3. Tidak mengoperasikan komputer dan"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 335), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "alat-alat elektronik lainnya tanpa seijin"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 355), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "pengelola laboratorium"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 375), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "4. Dilarang meminjam barang-barang dan"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 395), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "alat-alat elektronink tanpa seijin"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 415), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "pengelola laboratorium"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 435), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "5. Dilarang membuang sampah sembarangan"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 455), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "6. Menjaga kebersihan dan kerapian ruangan"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 475), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "laboratorium"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 495), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "7. Dilarang berpindah-pindah tempat kecuali"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 515), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "seijin pengelola laboratorium"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 535), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "8. Volume suara standar / tidak menimbulkan"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 555), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "suara gaduh / tidak ribut"
font = cv.FONT_HERSHEY_PLAIN
fontsize = 1.1
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(117, 575), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "Tertanda,"
font = cv.FONT_ITALIC
fontsize = 0.4
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(285, 620), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "Pengelola Laboratorium Komputer dan Bahasa"
font = cv.FONT_ITALIC
fontsize = 0.4
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(285, 640), font,fontsize,textcolor,thickness, cv.LINE_AA)





#show
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows