N=int(input("Digite N: "))
def NumeroPerfecto(N):
    Suma=0
    for i in range(1,N):
        if (N%i==0):
            Suma+=i
    if(N==Suma):
        return(True)
    else:
        return(False)
if(NumeroPerfecto(N)):
    print(N," es un numero perfecto")
else:
    print(N," no es un numero perfecto")