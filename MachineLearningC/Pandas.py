'''La series son matrices de una dimension que almacenan datos homogeneos
puede tener valores de datos mutable e inmutables, tiene indices para cada columna'''

'''Los dataframes son estructuras de datos de dos dimensiones, este tiene datos heterogenos
y el tamaño, y los datos pueden ser mutables '''
import pandas as pd
import numpy as np

Data=np.array([["x","Col1","Col2"],["Fila1",11,22],["Fila2",33,44]])
DataF=pd.DataFrame(data=Data)
#Adicionando nueva columna
DataF['ColumnaNueva']=pd.Series([1,2,3])
print(DataF)
del DataF[1]#Eliminar datos
print(DataF)
DataF.pop('ColumnaNueva')#Eliminar columnas
print(DataF)
#Agregando nuevas filas
DataF2=pd.DataFrame([['Fila3',55,66],['Fila4',77,88]],columns=[0,1,2])
DataF=DataF.append(DataF2)
print(DataF)
#Seleccionar una fila con loc
print(DataF.loc[0])#En este dataframe existen dos filas 0
# Selecciona una fila por etiqueta

'''rta=Data.loc['a']
print(rta)'''

# Selecciona una fila por numero
'''Data.iloc[0]
print(Data.iloc[0])'''


print(pd.DataFrame(data=Data[1:,1:], index=Data[1:,0], columns=Data[0,1:]))
'''Sirve para establecer los indices tanto de las columnas como de las filas,
con data se empieza a contar la informacion desde la parte seleccionada'''
A=np.array([[11,22,33,44],[55,66,77,88],[99,100,111,122]])
df=pd.DataFrame(A, columns=['once','veintidos','treintatres','cuarentacuatro'])#Crea el dataframe
print(df)



DData=np.array(["Ivan","Jaider","Misael","Milena","Camilo"])
serie=pd.Series(data=DData)
print(serie)
print("Forma del DataFrame: ",Data.shape)
print("Altura del DataFrame: ",len(df.index))
print(df.index)

print(df)
print(df.describe())
'''El método describe devuelve información estadística de los datos
 del dataframe o de la serie (de hecho, este método devuelve un dataframe). 
 Esta información incluye el número de muestras, el valor medio, la desviación estándar, el valor mínimo, máximo, 
 la mediana y los valores correspondientes a los percentiles 25% y 75%.'''


