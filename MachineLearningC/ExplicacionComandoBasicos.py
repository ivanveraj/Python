#Tipos de datos y creacion de variables
Entero=10#Este tipo de dato en programacion se define como int
Decimal=11.5#Este tipo de dato en programacion se define como double o float
Caracteres="Hola, soy una cadena de texto"#Este tipo de dato en programacion se define como str
Booleano=True#Este tipo de dato en programacion se define como boolean

#Entrada y salida de datos
print("Estoy realizando una salida de datos")
print("Soy la variable Entero, el valor que tengo almacenado dentro de mi es: ",Entero)
#La coma se utiliza para concatenar cadena de caracteres y todo tipo de datos
Entero=input("Digite un valor para modificar el contenido: ")
print("Soy la variable Entero, mi valor es: "+Entero)

#Condicionales
Edad=int(input("Digite su edad: "))#La palabra int convierte lo obtenido en el input a un tipo entero
if(Edad>=18):#Condicion mayor o igual que 18
    print("Eres mayor de edad")
else:#Sino se cumple la condicion realice el siguiente proceso
    print("Eres menor de edad")

#Creacion de funciones
def Suma(A,B):#Para crear una funcion anteponer al nombre la palabra reservada def
    #A y B son parametros que la funcion pide
    SumaNum=A+B
    return SumaNum#Para retorna un valor palabra reservada return

S=Suma(5,10)#Se invoca la funcion con su nombre y se le debe enviar los parametros solicitados
#Como la funcion retorna un valor se puede almacenar dentro de una variable
print("La suma es: ",S)



