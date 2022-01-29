import sqlite3
Conexion=sqlite3.connect("Primera Base")
Cursor=Conexion.cursor()
#Cursor.execute("create table Productos(Articulo Varchar(50),Precio Integer,Seccion Varchar(20))")
#Cursor.execute("INSERT INTO PRODUCTOS VALUES('Balon',15,'Deportes')")
'''ProductosIns=[("Carro",15,"Juguetes")
    ,("Tableta",30,"Construccion")
    ,("Harina",2,"Cocina")
              ]
#Cursor.executemany("INSERT INTO Productos VALUES(?,?,?)",ProductosIns)
'''
Cursor.execute("SELECT * FROM Productos")
Pro=Cursor.fetchall()
print(Pro)
for i in Pro:
    print("Nombre producto:",i[0],"\nSeccion:",i[2],"\nPrecio",i[1])
Conexion.commit()
Conexion.close()