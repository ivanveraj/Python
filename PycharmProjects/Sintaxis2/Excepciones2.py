'''def Edad(E):
    if E<0:
        raise TypeError("No se permiten edades negativas")#Utilizar cualquier error
    elif E<20:
        print("Eres joven")
    elif E<40:
        print("Esta adulto")
    elif E<=100:
        print("Estas mayor")
Edad(10)'''
import math
def CalcRaiz(N):
    if(N<0):
        raise ValueError("Numero no puede ser negativo")
    else:
        print("Raiz de: ",N,"=",math.sqrt(N))
Num=int(input("Digite un numero\n"))
try:
    CalcRaiz(Num)
except ValueError as ErrorNumeroNegativo:#as para definir el error
    print(ErrorNumeroNegativo)
    print("El numero no puede ser negativo...")
print("Programa terminado")