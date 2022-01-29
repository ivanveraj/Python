def Pares(Limite):
    N=1
    V=[]
    while N<Limite:
        V.append(N*2)
        N+=1
    return V
def Generadores(Limite):
    N=1
    while N<Limite:
        yield N*2
        N=N+1
print(Pares(10))
R=Generadores(10)
for i in range(0,10,1):
    print(next(R))

