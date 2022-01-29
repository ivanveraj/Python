'''
De la siguiente matriz halle la traspuesta, diagonal, inversa y determinante,
todo esto utilizando metodos propios de la libreria numpy
Matriz=[[1,2,3],[4,5,6],[7,5,9]]
'''
import numpy as np
Arr=np.array([[1,2,3],[4,5,6],[7,5,9]])

'''Autor: Ivan Jaimes
Funcion: Traspuesta
Descripcion: funcion que recibe una matriz y calcula la traspuesta principal
de dicha matriz'''
def Traspuesta(Arr):
    Nuevo=Arr.T#Halla la traspuesta de una matriz
    print("Traspuesta")
    print(Nuevo)

'''Autor: Ivan Jaimes
Funcion: Diagonal
Descripcion: funcion que recibe una matriz y calcula la diagonal principal
de dicha matriz'''
def Diagonal(Arr):
    Nuevo=Arr.diagonal()#Halla la Diagonal de una matriz
    print("Diagonal")
    print(Nuevo)

'''Autor: Ivan Jaimes
Funcion: Traspuesta
Descripcion: funcion que recibe una matriz y calcula la determinante
de dicha matriz'''
'''La determinante es la suma de la diagonal principal
    menos la suma de la diagonal secundaria'''
def Determinante(Arr):
    Nuevo=np.linalg.det(Arr)
    print("Determinante")
    print(Nuevo)
print(Arr)
Traspuesta(Arr)
Diagonal(Arr)
Determinante(Arr)
