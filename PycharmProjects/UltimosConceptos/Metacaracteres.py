import re
Lista=[
    "Jaider Ivan Vera",
    "Nery Camilo Vera",
    "Misael Vera Villamizar",
    "Yebreil Enrique Villamizar",
    "Ana Milena Jaimes",
    "Niños",
    "Niñas"
]
for i in Lista:
    if(re.findall("Vera$",i)):# (#)Cadena que finalice con Vera
        print(i)
    if (re.findall("^Nery", i)):  # (^)Cadena que inicie con Nery
        print("Inicia: ", i)
print("------")
for i in Lista:
    if (re.findall("[J]", i)):#Busqueda de un caracter especifico
        print(i)
print("------")
for i in Lista:
    if (re.findall("Niñ[oa]s", i)):#Busqueda de un caracter variante
        print(i)