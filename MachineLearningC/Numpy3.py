import numpy as np
#Tupla vacia
Tupla=()
print(Tupla)
#Tupla de enteros
Tupla=(1,2,3,4)
print(Tupla)
#Tupla mixta
Tupla=(1,2.3,'Hola socio')
print(Tupla)
#Tupla anidada
Tupla=(1,2,(2.1,2.2,2.3))
print(Tupla[2])
#Desempaquetado de una tupla
Tupla=(1,2,3)
a,b,c=Tupla
print("A ",a," B",b," C ",c)

#Función que permite crear un arreglo de nxm con valores aleatorios
def ValoresAleatorios(Limite,Filas,Columnas):
    return np.random.randint(Limite,size=(Filas,Columnas))

#Función que permite crear un arreglo de nxm con valores aleatorios
#entre un rango dado
def ValoresAleatoriosRango(LimiteI,LimiteF,Filas,Columnas):
    return np.random.randint(LimiteI,LimiteF,size=(Filas,Columnas))
print(ValoresAleatorios(30,3,3))
print(ValoresAleatoriosRango(30,50,3,4))

Matriz3D=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(Matriz3D[1,1,2])#Primer numero la dimension, segundo la fila, tercer la columna

Recorridos=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(Recorridos[1:4])
Recorridos2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(Recorridos2[2:8:2])# 1N°=Inicio 2N°=Fin 3N°=Paso de la lista
print('\n')
#Recorrido de un ndarray
print(list(np.nditer(Recorridos)))
#Funcion concatenete
#Sirve para unir dos ndarray
A=np.array([1,2,3])
B=np.array([4,5,6])
C=np.concatenate((A,B))
print(C)

A=np.array([[1,2,3],[4,5,6]])
B=np.array([[7,8,9],[10,11,12]])
C=np.concatenate((A,B))
print(C)
C=np.concatenate((A,B),axis=1)#Axis permite combinar como un objeto unico
#Por defecto es Cero
print(C)
#Para dividir matrices se utiliza array_split
def Dividir(C,Size):
    Nuevo=np.array_split(C,Size)
    return Nuevo
print(Dividir(C,2))

C=np.array([1,2,3,4,5,6,8,15,9,10,11,42,30])
#Buscador de elementos where
def Buscador(C,Elemento):
    Index=np.where(C==Elemento)#Where retorna la posicion del valor buscado
    return Index
print(Buscador(C,2))
def ParesWhere(C):
    Index=np.where(C%2==0)
    return Index
print(ParesWhere(C))

def Sort(C):
    Ordenado=np.sort(C)#Ordena todo tipo de ndarray
    return Ordenado
print('Original: ',C)
print('Ordenado',Sort(C))

#Operaciones matematicas en Numpy

A=np.array([1,2,3,4,5,30])
B=np.array([1,2,3,4,5,30])
print('Suma',np.add(A,B))#Suma
print('Resta',np.subtract(A,B))#Resta
print('Multiplicacion',np.multiply(A,B))#Multiplicacion
print('Division',np.divide(A,B))#Division

Arr=np.array([[1,2,3],[4,5,6],[7,5,9]])
def Traspuesta(Arr):
    Nuevo=Arr.T#Halla la traspuesta de una matriz
    return Nuevo

def Diagonal(Arr):
    Nuevo=Arr.diagonal()#Halla la Diagonal de una matriz
    return Nuevo

def Inversa(Arr):
    Nuevo = np.linalg.inv(Arr)#Halla la Inversa de una matriz
    return Nuevo

def Determinante(Arr):
    Nuevo=np.linalg.det(Arr)#Halla la Determinante de una matriz
    #La determinante es la suma de la diagonal principal
    #menos la suma de la diagonal secundaria
    return Nuevo

print('Traspuesta',Traspuesta(Arr))
print('Diagonal',Diagonal(Arr))
print('Inversa',Inversa(Arr))#Solo recibe matricez cuadradas
print('Determinante',Determinante(Arr))#Solo recibe matricez cuadradas



