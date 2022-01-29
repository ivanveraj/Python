def Crear(F,C):
    M=[]
    while(F!=0):
        M.append([0]*C)
        F-=1
    return M

def Llenar(M):
    C=1
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j]=C
            C+=1
def Traspuesta(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if(i!=j and j>i):
                Aux=M[i][j]
                M[i][j] =M[j][i]
                M[j][i]=Aux
    return M

M=Crear(5,5)
Llenar(M)
print(M)
print(Traspuesta(M))
