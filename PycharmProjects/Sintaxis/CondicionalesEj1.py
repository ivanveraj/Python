#Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par, o si ambos lo son.
N1=float(input("Digite N1 "))
N2=float(input("Digite N2 "))
if(N1%2==0 and N2%2==0):
    print("Ambos son pares")
else:
    print("Numeros impares")
if((N1%2)==0):
    print(N1," es par")
else:
    print(N1," es impar")
if((N2%2)==0):
    print(N2," es par")
else:
    print(N2," es impar")
