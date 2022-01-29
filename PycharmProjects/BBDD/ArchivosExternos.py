from io import open
'''
1.Apertura
2.Modificacion
3.Cierre
'''
A=open("EjemploAE.txt","w")#W es Write Escritura
#Sino existe se crea un nuevo archivo con el nombre dado
Nombre="Nombre: Jaider Ivan Vera Jaimes\n"
Edad="Edad:17\n"
FechaC="Fecha de Cumpleaños: 8 de Octubre 2002\n"
A.write(Nombre)
A.write(Edad)
A.write(FechaC)
A.close()
AE=open("EjemploAE.txt","r")
Info=AE.read()
AE.close()
print(Info)
AE2=open("EjemploAE.txt","r")#r es lectura READ
Vec=AE2.readlines()
AE2.close()
print(Vec)
AE3=open("EjemploAE.txt","a")#a es modo append
AE3.write("Institucion: ISER\n")