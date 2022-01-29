import sqlite3
Conexion=sqlite3.connect("Base2")
Cursor=Conexion.cursor()

#Cursor.execute("DELETE FROM Productos WHERE id=5")

#Cursor.execute("UPDATE Productos SET Precio=35 WHERE Nombre='Pelota'")


'''Cursor.execute("SELECT * FROM Productos WHERE Seccion='Construccion' ")
ProductoLec=Cursor.fetchall()
for i in ProductoLec:
    print(i)'''


#Cursor.execute('''
#CREATE TABLE Productos (
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#Nombre VARCHAR(50) UNIQUE,
#Precio INTEGER,
#Seccion VARCHAR(20))
#''')
'''ProductosIns=[("Pelota",20,"Jugueteria"),
              ("Pantalon",30,"Confeccion"),
              ("Destornillador",25,"Ferreteria"),
              ("Jarron",33.3,"Construccion"),
              ("Jarrones",35,"Construccion")
              ]
'''
#Cursor.executemany("INSERT INTO Productos VALUES(NULL,?,?,?)",ProductosIns)
#Cursor.execute("INSERT INTO Productos VALUES('AR05','Tren',15,'Jugueteria')")
Conexion.commit()
Conexion.close()