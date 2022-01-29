A=int(input("Digite un numero A: "))
B=int(input("Digite un numero B: "))
C=int(input("Digite un numero C: "))
Mayor=0
Menor=0
if(A>B and A>C and B>C):
    Mayor=A
    Menor=C
elif(B>C and B>A and C>A):
    Mayor=B
    Menor=A
elif(C>A and C>B and A>B):
    Mayor=C
    Menor=B
elif(A>C and A>B and C>B):
    Mayor=A
    Menor=B
elif(B>A and B>C and A>C):
    Mayor=B
    Menor=C
elif(C>B and C>A and B>A):
    Mayor=C
    Menor=A
print("El numero mayor es: ",Mayor)
print("El numero menor es: ",Menor)