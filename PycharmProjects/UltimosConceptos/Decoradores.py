def Decoradora(Funcion):
    def DecoradoraInt(*args,**kwargs):# *args recibe el numero de parametros deseados
        print("Iniciando calculo")
        Funcion(*args,**kwargs)# **kwargs recibe clave-valor
        print("Calculo terminado")
    return DecoradoraInt
@Decoradora
def Suma(Num1,Num2,Num3):
    print(Num1+Num2+Num3)
@Decoradora
def Resta(Num1,Num2):
    print(Num1-Num2)
@Decoradora
def Potencia(Base,Exponente):
    print(pow(Base,Exponente))
Num1=45
Num2=64
Num3=12
Suma(Num1,Num2,Num3)
Resta(Num1,Num2)
Potencia(Base=5,Exponente=3)#Cuando se pasa clave-valor

