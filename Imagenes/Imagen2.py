import cv2
import numpy as np

Img=cv2.imread('ISER2.jpg')

lar,anc=Img.shape[:2]
#print(lar)
#print(lar*.15)
'''MatrizR=cv2.getRotationMatrix2D((anc/2,lar/2),90,.1)#Punto de rotacion
Rotacion=cv2.warpAffine(Img,MatrizR,(anc,lar))
cv2.imshow('Imagen',Rotacion)#Rotar imagenes'''

'''a=int(lar*.15)
b=int(lar*.85)
c=int(anc*.15)
d=int(anc*.85)
Img=Img[a:b,c:d]
#Recorte de una imagen'''

'''#Img=cv2.resize(Img,(0,0),fx=0.75,fy=0.75)
Img=cv2.resize(Img,(200,200))
#Redimensinar imagenes'''

'''Img=cv2.bitwise_not(Img)#Negativo'''

'''Img=cv2.addWeighted(Img,2.5,np.zeros(Img.shape,Img.dtype),0,0)
#Realce de contraste
'''
#Img=cv2.GaussianBlur(Img,(7,7),0)#Desenfoque reduccion de tamaño

Insta=cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)
gray_insta=cv2.medianBlur(cv2.cvtColor(Insta,cv2.COLOR_BGR2GRAY),3)
Circulos=cv2.HoughCircles(gray_insta,cv2.HOUGH_GRADIENT,1,20,param1=50,minRadius=0,maxRadius=0)
Circulos=np.uint16(np.around(Circulos))
Mask=np.full((Insta.shape[0],Insta.shape[1]),0,dtype=np.uint8)

for i in Circulos[0,:]:
    cv2.circle(Mask,(i[0],i[1]),i[2],(255,255,255),-1)

Img=cv2.bitwise_or(Insta,Insta,Mask)

cv2.imshow('Imagen',Img)
cv2.waitKey(0)
cv2.destroyAllWindows()