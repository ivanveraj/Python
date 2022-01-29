def Suma(num1,num2):
    return num1+num2
def Resta(num1, num2):
    return num1-num2
def Multiplica(num1, num2):
    return num1*num2
def Divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return("Division erronea")
    finally:#Se ejecuta despues de las lineas de codigo
        print("Calculo realizado")
while True:
    try:
        op1=(int(input("Introduce el primer numero: ")))
        op2=(int(input("Introduce el segundo numero: ")))
        break
    except ValueError:#Se pueden realizaar excepciones consecutiva EXCEPT
        print("Valores introducidos incorrectos intentalo de nuevo")
Op=int(input("Introduce la operacion a realizar\n([1]Suma\n[2]resta\n[3]Multiplicacion\n[4]Division)\n"))
if Op==1:
    print(Suma(op1, op2))
elif Op==2:
    print(Resta(op1, op2))
elif Op==3:
    print(Multiplica(op1, op2))
elif Op==4:
    print(Divide(op1, op2))
else:
    print("Operacion no contemplada")
print("Operacion ejecutada. Continuacion de ejecucion del programa ")