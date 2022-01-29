import matplotlib.pyplot as plt
import numpy as np
import math

'''Autora: Jineth Vanesa Tarazona Pico
Funcion formula(V,k,D)
    Calcula el potencia de morse y lo retorna
Parametros:
V: np.array
k: Real positivo
D: entero positivo  
Retorno:
R: Lista
    '''
def formula(V,k,D):
    j=0
    R=[]
    while(j<len(V)):
        R.append((-D)+(D)*math.pow((1-np.exp(-k*V[j])),2))
        j+=1
    print(R)
    return R
'''Autora: Jineth Vanesa Tarazona Pico
Funcion graficar(ax,V,k,D1,D2,D3)
    Grafica los datos que resultan de la formula de potencial de morse y se le aplican estilos
    a la grafica para tener una mejor visualizacion, se le adiciona una legenda para evidenciar la informacion
Parametros:
ax: perteneciente a matploitlib
V: np.array
k: Real positivo
D1: entero positivo  
D2: entero positivo
D3: entero positivo
Retorno:
Nulo
    '''
def graficar(ax,V,k,D1,D2,D3):
    ax.plot(V, formula(V, k, D1),linewidth=3.0)
    ax.plot(V, formula(V, k, D2),linewidth=3.0)
    ax.plot(V, formula(V, k, D3),linewidth=3.0)
    plt.xlabel("X")
    plt.ylabel("Ep(X)")
    plt.title("Potencial de Morse.")
    plt.legend({'Para D1', 'Para D2', 'Para D3'}, loc='upper right')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xlim(-3, 3)
    plt.ylim(-3.5, 3.5)
    plt.show()
'''Autora: Jineth Vanesa Tarazona Pico
Funcion funciongrafica(k,D1,D2,D3)
    Crea el np.array y la fig de matploit.lib
Parametros:
k: Real positivo
D1: entero positivo  
D2: entero positivo
D3: entero positivo
Retorno:
Nulo
    '''
def funciongrafica(k,D1,D2,D3):
    V = np.linspace(-1, 4)
    print("Numpy array")
    print(V)
    fig, ax = plt.subplots()
    graficar(ax,V,k,D1,D2,D3)
k=float(input("Digite k (0.83)\n"))
D1=int(input("Digite D1\n"))
D2=int(input("Digite D2\n"))
D3=int(input("Digite D3\n"))
print("Prueba")
funciongrafica(0.83,1,2,3)
funciongrafica(k,D1,D2,D3)
