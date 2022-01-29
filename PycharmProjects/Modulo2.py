'''import Modulo1
U=int(input("Digite un numero"))
D=int(input("Digite un numero"))
Modulo1.Multi(U,D)
Modulo1.Resta(U,D)
Modulo1.Sumar(U,D)'''
print("Otra forma")
from Modulo1 import Sumar
Sumar(5,6)
from Modulo1 import *#Mucho espacio de memoria
Multi(23,2)
from Paquetes.PaquetesPrueba import *
'''La carpeta debe estar dentro del proyecto, no se debe separar por carpetas cada proyecto
no deja importar'''
Info()
from Paquetes.DirDir.Saludo import *
SaludoA()
from Paquetes.PaquetesPrueba import *
Info()
