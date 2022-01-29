a=frozenset({1,2,3})#Con Frozenset se convierte en un conjunto inmutable
b={4,5,3}
C={1,2,3,4,5,6}
c=a|b#Union
d=a&b#Intersecion
e=a-b#Diferencia elemento que estan en a y no en b
f=a^b#Diferencia simetrica
print(a==b)#Compara
print(c)
print(d)
print(e)
print(f)
print(a.issubset(C))#a Es subconjunto de C
print(C.issuperset(a))#C es superconjunto de a
print(a.isdisjoint(b))#Disconexos no deben compartir ningun elemento