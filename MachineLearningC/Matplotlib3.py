import matplotlib.pyplot as plt
import numpy as np

'''def Exponencial(X):
    Y=2*np.exp(X)
    return Y
def GraficaExp(a,b):
    X=np.linspace(a,b,30)
    Y=Exponencial(X)
    plt.plot(X,Y)
    plt.show()
GraficaExp(-10,10)'''

def LogaritmoNeperiano(X):
    Y=np.log(X)
    return Y
def Logaritmo10(X):
    Y=np.log10(X)
    return Y
def Graficar(a,b):
    X=np.linspace(a,b,30)
    Y=LogaritmoNeperiano(X)
    Z=Logaritmo10(X)
    plt.plot(X,Y,color='red')
    plt.plot(X,Z)
    plt.show()
Graficar(1,10)