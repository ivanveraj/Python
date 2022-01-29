'''Programa que imprime un dataframe con los tipos de arboles y sus nombres,
ademas cuenta la cantidad de arboles ingresados segun el tipo e imprime la informacion 
en una serie de pandas'''
import pandas as pd
import numpy as np
def Contador(DF):
    print("Cantidad de arboles segun su tipo")
    Filas, Columnas=DF.shape
    j=0
    Cont=0
    V=[]
    while(j<Filas):
        if(DF.loc[j]['Hoja caduca']!='0'):
            Cont+=1
        j += 1
    V.append(Cont)
    Cont = 0
    j=0
    while (j < Filas):
        if (DF.loc[j]['Hoja perenne']!='0'):
            Cont += 1
        j += 1
    V.append(Cont)
    Cont = 0
    j = 0
    while (j < Filas):
        if (DF.loc[j]['Frutales']!='0'):
            Cont += 1
        j += 1
    V.append(Cont)
    Cont = 0
    j = 0
    while (j < Filas):
        if (DF.loc[j]['Ornamentales']!='0'):
            Cont += 1
        j += 1
    V.append(Cont)
    Serie=pd.Series(V)
    Serie.rename(index={0:'Hoja caduca',1:'Hoja perenne',2:'Frutales',3:'Ornamentales'}, inplace=True)
    print(Serie)

Data=np.array([["Cerezo","Pino","Aguacate","Arce coreano"],
               ["Almendro","Mimosa","Mango","Lilo"],
               ["Gingko","Acacia","Limonero","Mimosa"],
               ["Ciruelo","Madroño","Manzano","Sauce plateado"],
               ["Nogal","Árbol del Neem","Naranjo","Árbol del amor"],
               ["Álamo blanco","Eucalipto","0","Árbol del Hierro"],
               ["Fresno","Ficus","0","0"],
               ["0","Olivo","0","0"]])
print("Tabla de los tipos de arboles")
DF=pd.DataFrame(Data, columns=['Hoja caduca','Hoja perenne','Frutales','Ornamentales'])
print(DF)
Y=DF.loc[0]['Hoja caduca']
Contador(DF)