#Frecuencia fundamental
'''Autor: Ivan Jaimes
Funcion wSub0 que calcula la frecuencia fundamental
Parámetro:
    T= hace refencia al Periodo
Retorno:
    Numero float
Casos de prueba:
    wSub0(10)-->0.62832
    wSub0(5)-->1.25664
    wSub0(3)-->2.0944
'''
def wSub0(T):
    return (2*3.1416)/T

#Coeficientes
'''Autor: Ivan Jaimes
Funcion que calcula el coeficiente de aSub0
Retorno:
    Numero float positivo
Casos de prueba:
    CaSub0()-->1.5708
'''
def CaSub0():
    return 3.1416/2
'''Autor: Ivan Jaimes
Funcion que calcula el coeficiente de aSubn
Retorno:
    Numero float positivo
Casos de prueba:
    CaSubn(1)-->4.1416
    CaSubn(2)-->1.7854
    CaSubn(3)-->1.3490666666666666
'''
def CaSubn(n):
    return 1-(-1**n)/(n**2)*3.1416
'''Autor: Ivan Jaimes
Funcion que calcula el coeficiente de bSubn
Retorno:
    Numero float positivo
Casos de prueba:
    CbSubn(1)-->1.0
    CbSubn(2)-->0.5
    CbSubn(3)-->0.3333333333333333
'''
def CbSubn(n):
    return 1/n
'''potencia(pBase, pExpo)
Autor: Ivan Jaimes
Función que calcula la potencia de un numero dado su base y su exponente
Parámetros:
    pBase: Número entero positivo que corresponde a la base
    pExpo: Número entero positivo que corresponde al exponente
Retorno:
    rtaPot: Número entero positivo que corresponde al cálculo de la potencia
Caso de prueba
    potencia(2,5)--> 32 
    potencia(2,0)--> 1
    potencia(0,2)--> 0'''
def potencia(pBase, pExpo):
    rtaPot = 1
    if(pExpo >= 0):
        i = 0
        while(i < pExpo):
            rtaPot = rtaPot * pBase
            i = i+1
    return rtaPot

'''logaritmoNatural(n)
Autor: Ivan Jaimes
Función que calcula el logaritmo natural de un numero
Parámetros:
    n: número entero positivo, diferente de cero, al que se le va a calcular el ln.
Retorno:
    suma: Resultado de la aproximacion del ln utilizando series de maclaurin
Casos de prueba
    logaritmoNatural(2)-->0.6931471805599456
    logaritmoNatural(4)-->1.3862943611196328
    logaritmoNatural(5)-->1.6094379091477102'''
def LogaritmoN(x):
    Sum=0
    n=0
    x_2=x**2
    while (n<100):
        Sum=Sum+(potencia((x_2 - 1)/(x_2 +1 ),(2*n+1)))/(2*n+1)
        n = n + 1
    return Sum

#Series de Taylor
'''Autor: Ivan Jaimes
Función que calcula el factorial de un número
Parámetros:
    X: Número entero positivo, el cual va a ser calculado el factorial
Retorno:
    Numero entero positivo con el calculo del factorial
Casos de prueba:
    Factorial(5)-->120
    Factorial(6)-->720 
    Factorial(4)-->24'''
def Factorial(X):
    Fac=1
    while (X>1):
        Fac=Fac*X
        X=X-1
    return Fac

#Funcion de ayuda a serie de Taylor Seno, Coseno
'''Autor: Ivan Jaimes
Función que convierte un grado a radianes
Parámetros:
    Grado: numero el cual va a ser convertido a radianes
Retorno:
    Numero float en radianes
Casos de prueba:
    Grados_Radianes(180)-->3.1415999999999995
    Grados_Radianes(100)-->1.7453333333333332
    Grados_Radianes(90)-->1.5707999999999998'''
def Grados_Radianes(Grado):
    return (Grado*3.1416)/180

'''Autor: Ivan Jaimes
Función que calcula el seno de un angulo con las series de Taylor
Parámetros:
    Grado: numero el cual va a ser convertido a radianes, para su uso en la serie
    Rep: Cantidad de repetiones, entre mas repeticiones mas exacto es la serie
Retorno:
    Numero float
Casos de prueba:
    Seno(45,4)-->0.707107768241554
    Seno(100,4)-->0.9844041565950015
    Seno(80,5)-->0.9848092929190447'''
def Seno(Grado,Rep):
    Sin=0.0
    G = Grados_Radianes(Grado)
    for n in range(Rep):
            Sin+=((-1)**n * G**(2*n+1))/Factorial(2*n+1)
    return Sin

'''Autor: Ivan Jaimes
Función que calcula el coseno de un angulo con las series de Taylor
Parámetros:
    Grado: numero el cual va a ser convertido a radianes, para su uso en la serie
    Rep: Cantidad de repetiones, entre mas repeticiones mas exacto es la serie
Retorno:
    Numero float
Casos de prueba:
    Coseno(45,4)-->0.7071019160809304
    Coseno(100,4)-->-0.17571709127326152
    Coseno(80,5)-->0.17365260984377578'''
def Coseno(Grado,Rep):
    Cos= 0.0
    G=Grados_Radianes(Grado)
    for n in range(Rep):
        Cos+=((-1) ** n *G**(2*n))/Factorial(2 * n)
    return Cos

'''Autor: Ivan Jaimes
Función que calcula la serie de fourier, utlizando la cooperacion de otras funciones
Parámetros:
    X: Numero dado por el usuario
    T: Periodo dado por el usuario
    Rep: Cantidad de repetiones, entre mas repeticiones mas exacto es la serie
Retorno:
    Numero float, con el calculo realizado en la serie de Fourier
Casos de prueba:
    Serie_Fourier(45,4,4)-->-0.4879807962217698
    Serie_Fourier(100,4,4)-->-492.3499579870196
    Serie_Fourier(80,5,5)-->83.76103171876184'''
def Serie_Fourier(X,T,Rep):
    n=1
    Sigma=0.0
    while(n<Rep):
        Sigma+=(CaSubn(n)*Coseno(n*wSub0(T)*X,Rep))+(CbSubn(n)*Seno(n*wSub0(T)*X,Rep))
        n+=1
    Fourier=(CaSub0() / 2)+Sigma
    return Fourier
print(Serie_Fourier(45,4,4))
print(Serie_Fourier(100,4,4))
print(Serie_Fourier(80,5,5))
