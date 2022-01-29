import numpy as np
import pandas as pd
#df=pd.read_csv("Eje1Numpy.csv", sep=';',names=['Nombre','Apellido'])
#print(df)

Array=np.loadtxt('Eje1Numpy.csv',delimiter=';')
print(Array[0][1])
print(Array.shape)
print(Array.ndim) 