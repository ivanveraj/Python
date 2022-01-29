'''Colecciones - Ejercicio 1:
Escriba un programa donde tenga una lista y que, a continuación,
 elimine los elementos repetidos, por último mostrar la lista.'''
'''Vec=[1,2,3,4,5,6,7,8,1,2]
Conjunto=set(Vec)
Vec=list(Conjunto)
print(Vec)'''
Vec=[1,2,3,4,5,6,7,8,1,2]
Vec=list(set(Vec))
print(Vec)