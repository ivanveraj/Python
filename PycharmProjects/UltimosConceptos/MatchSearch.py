import re
N1="Jaider Ivan Vera"
N2="Misael Vera"
N3="Ana Milena"
N4="Laider jaimes"
if re.match("Jaider",N4,re.IGNORECASE):#Sensibilidad ante mayusculas
     print("Lo hemos encontradooo")
else:
    print("No lo hemos encontrado")
print("---")
if re.match(".aider",N4,re.IGNORECASE):
    print("Lo hemos encontrado")
    print(re.match.__doc__)
else:
    print("No lo hemos encontrado")

if re.search("Vera",N1):
    print("Apellido encontrado")
else:
    print("No lo hemos encontrado")
if re.search("Vera",N3):
    print("Apellido encontrado")
else:
    print("No lo hemos encontrado")