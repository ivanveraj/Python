''''Hacer un programa que simule un cajero automático con un saldo inicial de $1000
y tendrá el siguiente menú de opciones:
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir'''
Saldo=1000
Menu=int(input("Digite una opcion\n[1]Ingresar dinero en la cuenta\n[2]Retirar dinero de la cuenta"
               "\n[3]Mostrar dinero disponible\n[4]Salir\n"))
if(Menu==1):
    Ingreso=float(input("Digite cantidad de dinero a ingresar"))
    Saldo+=Ingreso
    print("Dinero: ",Saldo)
if(Menu==2):
    Ingreso = float(input("Digite cantidad de dinero a retirar"))
    if(Ingreso<=Saldo):
        Saldo -= Ingreso
        print("Dinero: ", Saldo)
    else:
        print("Monto incorrecto")
if (Menu == 3):
    print("Dinero disponible: $",Saldo)
if (Menu == 4):
    print("Gracias por ingresar")