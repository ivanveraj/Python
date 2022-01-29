'''def FCiudades(*Ciudad):
    for i in Ciudad:
        for j in i:
            yield j'''
def FCiudades(*Ciudad):
    for i in Ciudad:
            yield from i#Devuel secciones de un mismo elemento
Ciudades=FCiudades("Pamplona","Cucuta","Bogota","Medello")
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))
print(next(Ciudades))