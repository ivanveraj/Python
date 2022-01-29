import pandas as pd
import matplotlib.pyplot as plt

class ClaseDataFrame():
    df=0
    def __init__(self, Archivo):
        self.df=pd.read_csv(Archivo, delimiter=';', decimal=",")
    def __str__(self):
        print(self.df)
    def DiagramaLineas(self,titulo,labelX,labelY):
        fig, ax = plt.subplots()
        ax.set_title(titulo)
        plt.xlabel(labelX)
        plt.ylabel('Temperatura °C')
        ax.plot(self.df[labelX],self.df[labelY])
        plt.show()
    def DiagramaAreas(self,titulo,labelX,labelY):
        fig, ax = plt.subplots()
        ax.set_title(titulo)
        plt.xlabel(labelX)
        plt.ylim(22,25)
        plt.ylabel('Temperatura °C')
        ax.fill_between(self.df[labelX],self.df[labelY])
        plt.show()
    def ImpresionGraficas(self):
        self.DiagramaLineas("Observacion anual de la temperatura Colombia 1901-2020", 'Categoria', 'PromedioA')
        self.DiagramaAreas("Observacion anual de la temperatura Colombia 1901-2020", 'Categoria', 'PromedioA')
    def FiltroTemperatura(self):
        print("Filtro de temperatura mayor a 25°C")
        X=self.df[self.df['PromedioA'] >=25]
        print(X)
    def FiltroAA(self):
        print("Filtro de temperatura desde el año 2000")
        X=self.df[self.df['Categoria'] >=2000]
        print(X)

    def AAMasCalurosos(self):
        X= self.df.sort_values(by="PromedioA", ascending=False)
        print("10 años mas calurosos de los ultimos 120 años en Colombia")
        print(X.head(10))

    def Agrupamiento(self):
        X=self.df.groupby('PromedioA').mean()
        print(X)
    def PromedioTemperatura(self):
        X=0
        i=0
        while(i<len(self.df)):
            X=self.df['PromedioA'][i]
            i+=1
        print("Promedio de temperatura de los ultimos 120 años en Colombia: ",X)

Clase=ClaseDataFrame('ArchivoTemperaturaC.csv')
Clase.__str__()
Clase.ImpresionGraficas()
Clase.FiltroTemperatura()
Clase.FiltroAA()
Clase.FiltroTemperatura()
Clase.Agrupamiento()
Clase.PromedioTemperatura()
