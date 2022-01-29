import pandas as pd
import matplotlib.pyplot as plt

class DataFrame:
    DataF=""
    def __init__(self, Archivo):
        self.DataF=pd.read_csv(Archivo, delimiter=';')
    def ImprimirDataFrame(self):
        print("El siguiente DataFrame posee informacion relacionada"
              "a la poblacion de dos paises, Colombia y Venezuela, diferenciadose "
              "entre las poblaciones urbanas y poblaciones totales")
        print(self.DataF)
    def GraficarDiagramaDispersion(self,EjeX, EjeY, NombreG,NombreX):
        fig, ax = plt.subplots()
        plt.title(NombreG)
        plt.xlabel(NombreX)
        plt.ylabel('Año')
        ax.scatter(self.DataF[EjeX], self.DataF[EjeY])
        plt.show()

    def GraficarDiagramaLineas(self,EjeX, EjeY, NombreG,NombreX):
        fig, ax = plt.subplots()
        plt.title(NombreG)
        plt.xlabel(NombreX)
        plt.ylabel('Año')
        ax.plot(self.DataF[EjeX], self.DataF[EjeY])
        plt.show()

    def GraficarDiagramaAreas(self, EjeX, EjeY, NombreG, NombreX):
        fig, ax = plt.subplots()
        plt.title(NombreG)
        plt.xlabel(NombreX)
        plt.ylabel('Año')
        ax.fill_between(self.DataF[EjeX], self.DataF[EjeY])
        plt.show()

    def MenuGraficas(self):
        while(True):
            Op=int(input("Digite la opcion que desee para graficar\n[1]Grafico de dispersion\n"
                         "[2]Grafico de lineas\n[3]Grafico de areas\n[4]Salir\n"))
            if(Op==1):
                self.GraficarDiagramaDispersion('Año', 'ColombiaU', 'Colombia: Poblacion urbana', 'P Urbano')
                self.GraficarDiagramaDispersion('Año', 'ColombiaT', 'Colombia: Poblacion total', 'P Total')
                self.GraficarDiagramaDispersion('Año', 'VenezuelaU', 'Venezuela: Poblacion urbana', 'P Urbano')
                self.GraficarDiagramaDispersion('Año', 'VenezuelaT', 'Venezuela: Poblacion total', 'P Total')
            elif Op==2:
                self.GraficarDiagramaLineas('Año', 'ColombiaU', 'Colombia: Poblacion urbana', 'P Urbano')
                self.GraficarDiagramaLineas('Año', 'ColombiaT', 'Colombia: Poblacion total', 'P Total')
                self.GraficarDiagramaLineas('Año', 'VenezuelaU', 'Venezuela: Poblacion urbana', 'P Urbano')
                self.GraficarDiagramaLineas('Año', 'VenezuelaT', 'Venezuela: Poblacion total', 'P Total')

            elif Op==3:
                self.GraficarDiagramaAreas('Año', 'ColombiaU', 'Colombia: Poblacion urbana', 'P Urbano')
                self.GraficarDiagramaAreas('Año', 'ColombiaT', 'Colombia: Poblacion total', 'P Total')
                self.GraficarDiagramaAreas('Año', 'VenezuelaU', 'Venezuela: Poblacion urbana', 'P Urbano')
                self.GraficarDiagramaAreas('Año', 'VenezuelaT', 'Venezuela: Poblacion total', 'P Total')
            elif Op==4:
                print("Saliendo del menu")
                break
    def FiltroPoblacionUrbana(self):
        print("Años en los cuales la poblacion urbana excedan a mas de 25 millones de personas")
        Op=int(input("Digite el pais a seleccionar\n[1]Colombia\n[2]Venezuela\n"))
        if(Op==1):
            DF=self.DataF[self.DataF['ColombiaU']>25000000]
            print(DF[['Año','ColombiaU']])
        elif Op==2:
            DF = self.DataF[self.DataF['VenezuelaU'] > 25000000]
            print(DF[['Año','VenezuelaU']])
        else:
            print("Error: codigo no valido")
    def AniosConMayorPoblacionTotal(self):
        print("Ultimos 5 años con la mayor poblacion de los paises: Colombia, Venezuela")
        Op = int(input("Digite el pais a seleccionar\n[1]Colombia\n[2]Venezuela\n"))
        if (Op == 1):
            dfordenado = self.DataF.sort_values(by="ColombiaT", ascending=False)
            print("Años con la mayor poblacion total en Colombia")
            print(dfordenado.head(5))
            print(dfordenado.head(5)[['Año','ColombiaT']])
        elif Op == 2:
            dfordenado = self.DataF.sort_values(by="VenezuelaT", ascending=False)
            print("Años con la mayor poblacion total en Venezuela")
            print(dfordenado.head(5))
            print(dfordenado.head(5)[['Año','VenezuelaT']])
        else:
            print("Error: codigo no valido")
    def Agrupamiento(self):
        X=self.DataF.groupby('Año')['ColombiaT']
        print(X.sum())
        print()

'''
Autores
Mayra Alejandra Siachoque Cachay
1006555791
Esteban Becerra Arismendy
1006636693
Kenny Camilo Cabrera Muñeton
1117550872'''
D=DataFrame('Poblacion Urbana.csv')
D.ImprimirDataFrame()
D.Agrupamiento()
D.AniosConMayorPoblacionTotal()
D.FiltroPoblacionUrbana()
D.MenuGraficas()
