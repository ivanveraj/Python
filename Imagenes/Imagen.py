import cv2
from matplotlib import pyplot as plt
import numpy as np
Img=cv2.imread('ISER1.png',1)
Img2=cv2.imread('ISER2.jpg',1)
'''print(Img.shape)
print(Img.size)
print(Img.dtype)'''

'''
print(Img2.shape)'''

'''cv2.imshow('Image',Img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''cv2.namedWindow("Imagen",cv2.WINDOW_NORMAL)
cv2.imshow("Imagen",Img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#cv2.imwrite("Prueba.png",Img)


'''plt.imshow(Img,cmap='gray',interpolation='bicubic')#La interpolacion permite mejorar los pixeles
plt.xticks([])
plt.show()'''

'''Copy=Img[125:185,100:160]
Img[10:70,80:140]=Copy
cv2.imshow('Image',Img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''rows,cols,channels=Img.shape
ro1=Img2[0:rows,0:cols]
ImgGray=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(ImgGray,10,255,cv2.THRESH_BINARY)
mask_inv=cv2.bitwise_not(mask)
Img1_bg=cv2.bitwise_and(ro1,ro1,mask=mask_inv)
Img2_fg=cv2.bitwise_and(Img,Img,mask=mask_inv)
dst=cv2.add(Img1_bg,Img2_fg)
Img2[0:rows,0:cols]=dst
cv2.imshow('Imagenn',Img2)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

Img3=cv2.imread('Ajedrez.jpg',1)
gray=cv2.cvtColor(Img3,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
dst=cv2.cornerHarris(gray,2,3,0.04)#Reconoce los bordes
dst=cv2.dilate(dst,None)
Img3[dst>0.01*dst.max()]=[0,0,255]#Color rojo
cv2.imshow('dst',Img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

