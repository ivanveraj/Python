'''
Programa que recibe un numero entero cuenta la cantidad de digitos, determina si es
o no capicua, y el resultado lo invierte
'''
def EsCapicua(X):
    if(str(X)==str(X)[::-1]):
        return True
    else:
        return False
def Digitos(X):
    Cont=0
    while(X>0):
        X=int(X/10)
        Cont+=1
    return Cont
def NuevoNum(X):
    Cadena=""
    while (X > 0):
        Aux=X%10
        X = int(X / 10)
        if(Aux%2==0):
            Cadena=Cadena+str(Aux)
    return int(Cadena)
Num=int(input("Digite un numero: "))
print("Numero ingresado: ",Num)
print("La cantidad de digitos del numero: ",Digitos(Num))
print("El numero es capicua: ",EsCapicua(Num))
print("Nuevo numero: ",NuevoNum(Num))

