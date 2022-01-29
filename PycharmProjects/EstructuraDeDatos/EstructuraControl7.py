N=int(input("Digite un numero: "))
Par=0
Impar=0
while(N!=0):
    Aux=N%10
    N=int(N/10)
    if(Aux%2==0):
        Par=Par+Aux
    else:
        Impar=Impar+Aux
print("Suma pares: ",Par)
print("Suma impares: ",Impar)