import re
C="Voy a aprender expresiones regulares en Python. Servira Python para mis proyectos"
TextoBuscar=re.search("aprender",C)
'''
if(re.search(TextoBuscar,C) is not None):
    print("Texto encontrado")
else:
    print("Texto no he encontrado")'''

print(TextoBuscar.start())#Devuelve la posicion inicial de la cadena encontrada
print(TextoBuscar.end())#Devuelve la posicion final de la cadena encontrada
print(TextoBuscar.span())#Hace lo mismo que Start y End
print(re.findall("Python",C))#Devuelve el numero de veces encontradas la palabra a buscar


