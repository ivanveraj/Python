#Listas
V=[1,2,3,4,20.4,1,1]#Lista dinamica
V.append("Ivan")#Agrega un elemento al final del vector
V.insert(4,5)#Inserta elemento en el indice 2, valor 40
V.extend(["Final","Final2"])#Se pasa un vector y se agrega al final
#La suma de vectores es L3=L1+L2
V.pop(2)#Elimina el numero 3 ubicado en el indice 2
V.remove("Final")#Elimina valor a eliminar de la lista
V.reverse()#Gira el vector
V.sort()#Ordena de menor a mayor el vector
V.sort(reverse=True)#Ordena de mayor a menor el vector
print(V)
print(V[-1])#Lo toma como el ultimo de la lista [40]
print(V[0:3])# Imprime desde el inicio hasta el indice 3, se cuenta de 1++
print(V[:4])# Imprime desde el inicio hasta el indice 4, se cuenta de 1++
print(len(V))#Tamaño del vector
print(40 in V)#Pregunta si un valor esta en el vector
print(V.index(4))# Devuelve el indice del valor
print(V.count(1))#Cuantas veces se encuentra el valor
V.clear()#Elimina el vector
print(V)