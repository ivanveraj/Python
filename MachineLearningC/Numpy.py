import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)
print()
b=np.array([[1,2,3],[4,5,6]],dtype=int)
print(b)

M=np.ones((4,5))#Para rellenar una matriz de puros ceros recibe N de filas y columnas
print(M)

M2=np.zeros((3,4))#Para rellanar una matriz con ceros recibe fila y columnas
print(M2)

M3=np.random.random((5,4))#Para rellenar una matriz con numeros aleatorios
print(M3)

M4=np.empty((4,4),dtype=float)#Crea un matriz vacia
print("Vacia", M4)

M5=np.full((2,2),"08")
print(M5)

e = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(e.T)#Para imprimir la transpuesta

e = np.array([[1,2,3],[4,5,6],[7,8,9]])
f = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Dot",f.dot(e))#Se multiplica de forma paralela y se suman
#Aun no se como funciona


Espaciador1=np.arange(2,8,1)#Llene un vector con 2 como valor inicial, termine en 8, con saltos de 1 en 1
print(Espaciador1)

Espaciador2=np.linspace(0,2,5)#Rellenar un vector con 5 valores que se encuentre entre 0 y 2
print(Espaciador2)

Identidad1=np.eye(4,3)#Crea una matriz con una diagonal de puros 1 y el resto llenos de ceros
print(Identidad1)
Identidad2=np.identity(5)#Crea una matriz cuadrada de tamaño 5
print(Identidad2)
print("Dimension del arreglo",Identidad2.ndim)
print("Tipo de datos almacenados",Identidad2.dtype)
print("Cantidad de filas y columnas",Identidad1.shape)
print("Cantidad de elementos en la columna",Identidad1.size)
#Operaciones con matrices
print(a+b)
print(a-b)
print(a/b)
print(a*b)
b=b.reshape(3,2)# Cambiar la forma de la matriz
# o
print(np.reshape(b,(3,3)))
print(b)



