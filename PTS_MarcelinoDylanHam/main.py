import cv2 as cv

img = cv.imread("white.png")

tinggi, lebar, _ = img.shape #600 800

#shape
cv.rectangle(img, (0,0), (600, 800),(0,0,0),-1)
cv.rectangle(img, (265,470), (335, 470),(0,190,255),-1)

#pak kalo saya liat di google FONT_HERSHEY_COMPLEX itu mirip dgn yang di gambar aslinya tapi disini
#kayak gaberubah pak fontnya bingung saya jadi agak kurang bagus

#draw text
text = "“Janganlah kamu berbuat seolah-"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (255,255,255) #white
thickness = thickness= 2
cv.putText(img, text,(85, 170), font,fontsize,textcolor,thickness, cv.LINE_AA)



text = "olah kamu mau memerintah atas"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(95, 220), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "mereka yang dipercayakan"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(130, 270), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "kepadamu, tetapi hendaklah"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(85, 320), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "kamu"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (0,190,255) #old gold orange
thickness = thickness= 2
cv.putText(img, text,(450, 320), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "menjadi"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (0,190,255)
thickness = thickness= 2
cv.putText(img, text,(125, 370), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "TELADAN"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 1.3
textcolor = (0,190,255)
thickness = thickness= 2
cv.putText(img, text,(240, 370), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "bagi"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (255,255,255) 
thickness = thickness= 2
cv.putText(img, text,(430, 370), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "kawanan domba itu.”"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (255,255,255)
thickness = thickness= 2
cv.putText(img, text,(170, 420), font,fontsize,textcolor,thickness,cv.LINE_AA)

text = "1 Petrus 5:3"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.9
textcolor = (255,255,255) 
thickness = thickness= 2
cv.putText(img, text,(220, 530), font,fontsize,textcolor,thickness, cv.LINE_AA)

text = "@ayatalkitabhiburan"
font = cv.FONT_HERSHEY_COMPLEX
fontsize = 0.5
textcolor = (255,255,255) 
thickness = thickness= 2
cv.putText(img, text,(221, 700), font,fontsize,textcolor,thickness, cv.LINE_AA)






#show
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows