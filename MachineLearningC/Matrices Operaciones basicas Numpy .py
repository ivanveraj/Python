'''Realice las operacion basicas utilizando el array (a) y (b), debe crear dichas matrices
con el uso de la libreria numpy, ademas se debe realiza un metodo para cada operacion'''
import numpy as np
'''Autor: Ivan Jaimes
Funcion: Suma
Descripcion: funcion que recibe dos matrices a y b para realizar la suma de cada
posicion e imprime el resultado'''
def Suma(a,b):
    print("Suma")
    print(a+b)

'''Autor: Ivan Jaimes
Funcion: Resta
Descripcion: funcion que recibe dos matrices a y b para realizar la resta de cada
posicion e imprime el resultado'''
def Resta(a,b):
    print("Resta")
    print(a-b)

'''Autor: Ivan Jaimes
Funcion: Division
Descripcion: funcion que recibe dos matrices a y b para realizar la divison de cada
posicion e imprime el resultado'''
def Division(a,b):
    print("Division")
    print(a/b)

'''Autor: Ivan Jaimes
Funcion: Multiplicacion
Descripcion: funcion que recibe dos matrices a y b para realizar la multiplicacionde cada
posicion e imprime el resultado'''
def Multiplicacion(a,b):
    print("Multiplicacion")
    print(a*b)

#Operaciones con matrices
a=np.array([[1,2,3],[4,5,6]],dtype=int)
b=np.array([[7,8,9],[10,11,12]],dtype=int)
print("Matriz (a)\n",a)
print("\nMatriz (b)\n",b)
Suma(a,b)
Resta(a,b)
Multiplicacion(a,b)
Division(a,b)
