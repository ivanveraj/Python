import pandas as pd


'''df = pd.DataFrame([[1,2],[3,4]], columns=['a','b'])
print('DataFrame.////\n')
print(df)
print('1.Axes.////\n')
print(df.axes)
print('2.Retorna los tipos de datos de los objetos/\n')
print(df.dtypes)
print('3.Verdadero si df está completamente vacío\n')
print(df.empty)
print('4.Número de axes\n')
print(df.ndim)
print('5.Retorna una tupla representando la dimensionalidad del DataFrame.\n')
print(df.shape)
print('6.Número de elementos en el df.\n')
print(df.size)
print('7.Representacion Numpy de un df.\n')
print(df.values)
print('8.Devuelve las primeras n filas. Cero no existe inicia en 1\n')
print(df.head(2))
print('9.Devuelve las últimas n filas. Cero no existe inicia en 1\n')
print(df.tail(2))'''

#Lectura de archivos
'''
Txt1=pd.read_fwf('datos.txt')
print(Txt1,'\n')
#Imprimir por cada columna
print(Txt1['Documento'],'\n')
print(Txt1['Nombre'],'\n')
print(Txt1.Nombre,'\n')'''

'''
#Leer un archivo que esta separado por comas (también puede ser por tabulador '\t'
Txt2= pd.read_csv('datos1.txt', delimiter='\t',header=0,index_col=0)
#header determina cual fila es el encabezado
#index_col determina la columna indice, tambien se le puede colocar un string 'Nombre'
print(Txt2)'''


Txt4=pd.read_csv('datos4.txt', delimiter='\t')
#Información del axes
print(Txt4.axes)

#Información de los datos
rta=Txt4.info()

#Función para obtener el mínimo
Min=Txt4['edad'].min()
print("Minimo de la columna edad",Min,'\n')

# Información y cálculos estadísticos de los datos
rta=Txt4["edad"].describe()
print(rta,'\n')

#Cuanto si una columna tiene informacion 30 columnas, 29 telefonos
Cuantos=Txt4['telefono'].count()
print(Cuantos,'\n')

# utilizando agrupación para obtener la cantidad de datos
dfporsexo=Txt4.groupby("genero").size().reset_index(name='TotalporSexo')
#reset_index crea una tabla y establece la nueva columna con un name dado
print(dfporsexo)
# utilizado para obtener el listado de personas según el genero
dfporsexo2=Txt4.groupby("genero")["nombre"]
print(list(dfporsexo2),'\n')
