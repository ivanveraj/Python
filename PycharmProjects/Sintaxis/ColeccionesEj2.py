'''Colecciones - Ejercicio 2:
Escriba un programa que tenga dos listas y que, a continuación,
cree las siguientes listas (en las que no debe haber repeticiones):
- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas.'''
V1=[1,2,3,4,5,6,7,8]
V2=[2,3,4,5,6,7,0,9,8,78]
C1=set(V1)
C2=set(V2)
Union=list(C1|C2)
SoloA=list(C1-C2)
SoloB=list(C2-C1)
Intercepcion=list(C1&C2)
print("Lista de elementos que aparecen en las dos listas: ",Union)
print("Lista de elementos que aparecen en la primera lista, pero no en la segunda: ",SoloA)
print("Lista de elementos que aparecen en la segunda lista, pero no en la primera: ",SoloB)
print("Lista de elementos que aparecen en ambas listas: ",Intercepcion)