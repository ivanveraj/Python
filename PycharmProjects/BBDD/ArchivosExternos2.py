from io import open
AE=open("EjemploAE.txt","r+")#r+ significa que esta en Modo Lectura-Escritura
'''print(AE.read())
AE.seek(0)#Al finalizar el metodo read posiciona el curso en la pos Final
#Metodo seek devuelve el cursor en el caracter dado
print(AE.read(10))#El metodo read imprime hasta el caracter dado
AE.write("Profesion: Estudiante\n")'''
Vec=AE.readlines()
print(Vec)
Vec[1]="Linea agregada desde el exterior\n"
AE.seek(0)
AE.writelines(Vec)
AE.close()
