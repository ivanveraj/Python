import numpy as np
import math
import matplotlib.pyplot as plt
'''Autor: Kenny Camilo Cabrera Muñeton 1117550872
Funcion PotencialDeMorse(k,X,D)
    Calcula el potencial de morse segun la formula entregada y retorna un vector con los resultados
    obtenidos esto con la misma cantidad de datos para graficar
Parametro:
    k:float
    X: array numpy
    D: entero
retorno:
    Array'''
def PotencialDeMorse(k,X,D):
    Ep=[]
    i=0
    while(i<len(X)):
        R=(-D)+(D)*math.pow((1-np.exp(-k*X[i])),2)
        Ep.append(R)
        i+=1
    return Ep
'''Autor: Kenny Camilo Cabrera Muñeton 1117550872
Funcion Graficar(k,X,D,D2,D3)
    Recibe todos lo parametros necesarios para imprimir una grafica que tenga 3 lineas unidas
    esto lo hace con la libreria matploitlib
Parametro:
    k:float
    X: array numpy
    D: entero
    D2: entero
    D3: entero
retorno:
    No retorna'''
def Graficar(k,D,D2,D3):
    fig, ax = plt.subplots()
    X=np.linspace(-1, 4)
    P=PotencialDeMorse(k,X,D)
    P2 = PotencialDeMorse(k, X, D2)
    P3 = PotencialDeMorse(k, X, D3)
    ax.plot(X,P)
    ax.plot(X,P2)
    ax.plot(X, P3)
    plt.xlim(-3,3)
    plt.ylim(-3.5,3.5)
    plt.xlabel("X")
    plt.ylabel("Ep(X)")
    plt.title("Potencial de Morse")
    plt.legend({'Para D=1','Para D=2','Para D=3'},loc='upper right')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    plt.show()
Graficar(0.83,1,2,3)
