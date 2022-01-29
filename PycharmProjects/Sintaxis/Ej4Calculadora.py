''''Condicionales - Ejercicio 4:
Construir un programa que simule el funcionamiento de una calculadora que puede realizar
las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división).
El usuario debe especificar la operación con el primer carácter  del nombre de la operación.
S, s – Suma
R, r – Resta
P, p, M, m – Multiplicación
D, d - División'''
N1=0
N2=0
Op=0
Operacion=input("Digite la operacion: ")
if(Operacion=="*"):
    N1=float(input("Digite N1: "))
    N2 = float(input("Digite N1: "))
    Op=N1*N2
    print("Multiplicacion: ",N1,"*",N2,"= ",Op)
if(Operacion=="+"):
    N1=float(input("Digite N1: "))
    N2 = float(input("Digite N2: "))
    Op=N1+N2
    print("Suma: ",N1,"+",N2,"= ",Op)
if(Operacion=="-"):
    N1=float(input("Digite N1: "))
    N2 = float(input("Digite N1: "))
    Op=N1-N2
    print("Suma: ",N1,"-",N2,"= ",Op)
if(Operacion=="/"):
    N1=float(input("Digite N1: "))
    N2 = float(input("Digite N1: "))
    Op=N1/N2
    print("Suma: ",N1,"/",N2,"= ",Op)