import re
Lista=[
    "Jaider Ivan Vera",
    "Nery Camilo Vera",
    "Misael Vera Villamizar",
    "Yebreil Enrique Villamizar",
    "Ana Milena Jaimes",
]
for i in Lista:
    if(re.findall("[J-N]",i)):#Rango desde la J hasta la N
        print(i)

Lista2=[
    "Ma1",
    "Se1",
    "Se2",
    "Ma2",
    "Ma3",
    "Ba1",
    "Ba2",
    "MaA",
    "MaC",
    "MaB",
    "Ma1A",
    "Se1A",
    "Se2A",
    "Ma2B",
    "Ma3C"
]
for i in Lista2:
    if(re.findall("Ma[0-3B-C]",i)):
        print(i)