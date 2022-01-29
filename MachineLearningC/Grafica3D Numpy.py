'''
Programa que utiliza diferentes librerias para la creacion de graficos en 3D, siendo este programa
un graficador de una linea en 3D curveado segun los valores ingresados
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Grafico3D_Uno(X,Y):
    Z=(X*X)-Y-6
    return Z
def GraficoLineal3D():
    Fig=plt.figure()
    Axes=Axes3D(Fig)#Crea un objeto de ejes 3D
    X=np.linspace(-4,4,50)
    Y=np.linspace(-4,4,50)
    Axes.plot(X,Y,Grafico3D_Uno(X,Y))#Recibe los tres parametros, ancho, altura, profundidad
    plt.show()

def GraficoSolido3D(EjeX=(0,1),EjeY=(0,1)):
    X1,X2=EjeX
    Y1,Y2=EjeY
    Fig=plt.figure()

    Axes=Axes3D(Fig)
    X=np.arange(X1,X2,0.25)
    Y=np.arange(Y1,Y2,0.25)
    print(X)
    print(Y)
    X,Y=np.meshgrid(X,Y)#Crea dos matrices cuadradas con los valores ingresados
    #Una matriz normal y la otra inversa
    print(X)
    print(Y)
    Z=Grafico3D_Uno(X,Y)
    Axes.plot_surface(X,Y,Z,cstride=1,rstride=1,cmap=plt.cm.hot)
    Axes.set_xlabel('Magnitud')
    plt.show()


#GraficoLineal3D()
GraficoSolido3D(EjeX=(-20,10),EjeY=(-20,20))