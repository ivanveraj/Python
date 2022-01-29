'''
Programa que grafica el seno, coseno y una parabola con matplotlib.pyplot y numpy
'''
import matplotlib.pyplot as plt
import numpy as np

def Parabola(X):
    Y=X*X-3*X-1
    return Y
def GraficarParabola(a,b):
    X=np.linspace(a,b,100,dtype='int')
    print(X)
    Y=Parabola(X)
    plt.plot(X,Y)
    plt.show()

def Seno(X):
    Y=np.sin(X)
    return Y

def Coseno(X):
    Y=np.cos(X)
    return Y

def Graficar(a,b):
    X=np.linspace(a,b,100)
    Sen=Seno(X)
    Cos=Coseno(X)
    plt.plot(X,Sen,color='red',marker='*')
    plt.plot(X,Cos,color='blue')
    plt.show()
Graficar(-6,6)
GraficarParabola(-50,50)