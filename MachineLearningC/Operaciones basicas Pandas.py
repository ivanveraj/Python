'''
Programa que realiza operaciones basicas utilizando series de la libreria Pandas
'''
import pandas as pd
def Operaciones(Serie1,Serie2):
    S=Serie1+Serie2
    print("Suma: \n",S)
    S = Serie1 - Serie2
    print("Resta: \n", S)
    S = Serie1 * Serie2
    print("Multiplicacion: \n", S)
    S = Serie1 / Serie2
    print("Division: \n", S)

def OperacionesLogicas(Serie1,Serie2):
    S = Serie1 < Serie2
    print("Comparacion serie 1 < serie 2: \n", S)
    S = Serie1 > Serie2
    print("Comparacion serie 1 > serie 2: \n", S)
def Digitar(Cant):
    i=0
    V=[]
    while(i<Cant):
        print("Posicion ",i)
        X = int(input("Digite un dato\n"))
        V.append(X)
        i+=1
    return V
Serie1 = pd.Series([1, 2, 3, 4, 5])
Serie2 = pd.Series([6, 7, 8, 9, 10])
Operaciones(Serie1,Serie2)
OperacionesLogicas(Serie1,Serie2)
Cant=int(input("Digite la cantidad de datos a insertar\n"))
print("Serie 1")
S1=Digitar(Cant)
Se1=pd.Series(S1)
print("Serie 2")
S2=Digitar(Cant)
Se2=pd.Series(S2)
Operaciones(Se1,Se2)
OperacionesLogicas(Se1,Se2)