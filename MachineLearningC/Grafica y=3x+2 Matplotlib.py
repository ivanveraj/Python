'''
Programa que grafica una recta y=3x+2 con matplotlib.pyplot y numpy
'''
import matplotlib.pyplot as plt
import numpy as np
'''plt.plot(2,5,marker='.',color='red')
plt.plot(1,5,marker='D',color='#02314F')#Tambien permite hexadecimal
plt.plot(7,5,marker='o',color='red')
plt.plot(8,5,marker='v',color='red')
plt.plot(9,5,marker='^',color='red')
plt.plot(2,4,marker='*',color='red')# 1° Eje X 2° Eje Y
#Marker sirve para dar una figura
#plot se utiliza para poner un punto en una posicion determinada
plt.show()'''
def Recta(X):
    y=3*X+2
    return y
def Graficar(a,b):
    X = np.linspace(A, B, 6, dtype=int)
    Y=Recta(X)
    plt.plot(X,Y)#Tambien crea lineas
    plt.show()
A=5
B=13
Graficar(A,B)


