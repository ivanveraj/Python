import matplotlib.pyplot as plt
import numpy as np

#GRAFICO 1
'''
X=np.arange(100)
Y=np.random.rand(100)
plt.plot(X,Y,color='black',label='X,f(x)')
plt.plot(X[Y>=0.85],Y[Y>=0.85],'bo',label='f(x)>=0.85')#Con bo se coloca una bola en la zona indicada
plt.axhspan(0.85,1,alpha=0.5)#Alpha da mayor contraste a la banda (Valores entre 0 y >1)
#axhspan coloca un subrayado sobre la zona indicada
plt.ylim(0,1.2)#Establece un limite en el eje Y
plt.legend()#La leyenda muestra los label graficados
plt.title('Grafica de representacion (X,f(x))')#Coloca titulo a la grafica
plt.xlabel('Valores de X')#Nombra el eje X
plt.ylabel('Valores de f(x)')#Nombra el eje Y
plt.grid(True)#Coloca cuadricula a la grafica
plt.show()'''

#GRAFICO 2

plt.axes()
plt.plot(np.exp(np.linspace(0,10,100)))
plt.axes([0.2,0.55,0.3,0.3],facecolor='gray')
#plt.axes(), 1°A= una tupla o lista con 4 valores
#1=Izquierda 2=Fondo 3=Ancho 4=Largo
#Los **kwargs son argumentos que le dan caracteristicas a los metodos
plt.plot(np.sin(np.linspace(0,10,100)),'bo',linewidth=2)
plt.show()