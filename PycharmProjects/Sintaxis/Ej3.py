#Hacer un programa que pida un carácter e indique si es una vocal o no.
Letra= input("Digite un caracter").lower() #lower() para transformar en minuscula
if(Letra=="a" or Letra=="e" or Letra=="i" or Letra=="o" or Letra=="u"):
    print("Es una vocal")
else:
    print("No es una vocal")
Letra2= input("Digite un caracter").upper() #upper() para transformar en mayuscula
print(Letra2)