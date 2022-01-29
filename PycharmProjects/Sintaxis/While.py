import  math
N=int(input("Digite un numero"))
while N<0:
    print("Numero negativo")
    N = int(input("Digite un numero"))
print("Raiz cuadrada: ",math.sqrt(N))