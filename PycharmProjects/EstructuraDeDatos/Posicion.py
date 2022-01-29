def Recibir(X,Pos):
    while(Pos>0):
        Num=X%10
        X=int(X/10)
        Pos=Pos-1
    return(Num)
X=int(input("Digite un numero"))
Pos=int(input("Digite la posicion a buscar"))
print("Numero recibido ",Recibir(1234,3))
