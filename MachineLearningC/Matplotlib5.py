import matplotlib.pyplot as plt
import numpy as np

#Histograma
'''
X=np.random.randn(10000)
plt.hist(X,bins=20)#bins son los topes del histograma
#plt.hist crea un histograma parecido a un grafico de barras
plt.show()'''

#Grafico de barras
'''
Prima=600+np.random.randn(5)*10
Dias=np.array([1,2,3,4,5])
plt.axes((0.1,0.3,0.8,0.6))#Este nuevo grafico es innecesario
plt.bar(np.arange(5),Prima)#Eje X ,Eje Y
plt.ylim(550,650)
plt.title('Prima de trabajo')
plt.xticks(np.arange(5),Dias,rotation=45)
#El arange crea las posiciones, Dias le da los valores o etiqueta
#Rotation le genera un comportamiento es un **kwargs
plt.xlabel('Dias')
plt.ylabel('Prima')
plt.show()
'''
def Recta(X):
    Y=3*X+2
    return Y
def GraficaRecta(a,b,numFig):
    X=np.linspace(a,b,dtype='int')
    Fig=plt.figure(numFig)#plt.figure crea figuras o ventanas, por defecto inicia en 1
    Plano=Fig.gca()#Busca los ejes actuales, sino existen los crea
    Y=Recta(X)
    Plano.set_title('Prueba W')
    Plano.plot(X,Y)
    plt.show()
GraficaRecta(5,6,1)