import math
def Raiz(X):
    print("La raiz cuadrada de ",X," es:",math.sqrt(X))
    print(X," elevado al cubo es:",X**3)
def Mayor(X,Y,Z):
    if(X>Y and X>Z):
        print(X," es el numero mayor")
    elif(Y>Z and Y>X):
        print(Y," es el numero mayor")
    elif(Z>X and Z>Y):
        print(Z, " es el numero mayor")
    elif(X>Z and X>Y):
        print(X, " es el numero mayor")
    elif(Y>X and Y>Z):
        print(Y, " es el numero mayor")
    elif(Z>Y and Z>X):
        print(Z, " es el numero mayor")
def Edad(X):
    if(X>0 and X<=122):
        if(X<=17):
            print("Eres menor de edad")
        elif(X>=18):
            print("Eres mayor de edad")
            if(X<=40):
                print("Eres una persona adulta")
            elif(X>40):
                print("Eres lonjevo")
    else:
        print("Edad invalida")
A=int(input("[1]Calcular la raiz cuadrada y su elevacion al cubo "
            "\n[2]Determinar entre 3 numeros cual es el mayor\n"
            "[3]Rango de edad\n"))
if(A==1):
    X=float(input("Digite un numero "))
    Raiz(X)
elif(A==2):
    X=float(input("Digite X "))
    Y=float(input("Digite Y "))
    Z=float(input("Digite Z "))
    Mayor(X,Y,Z)
elif(A==3):
    X=float(input("Digite su edad: "))
    Edad(X)