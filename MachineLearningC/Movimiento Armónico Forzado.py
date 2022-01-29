'''Programa que grafica el Movimiento Armónico Forzado utilizando pyplot y numpy'''
import matplotlib.pyplot as plt
import numpy as np
import math

def C(F_sub0, m, w_sub0, omega, CoeR):
    Arm1=(F_sub0/(m*math.pow(w_sub0,2)))
    x=math.pow((1-math.pow((omega/w_sub0),2)),2)
    y=math.pow(((2*CoeR)*(omega/w_sub0)),2)
    Arm2=(1/math.sqrt(x+y))
    return(Arm1*Arm2)

def Graficar():
    ax=plt.axes()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    CoeR=np.array([0.1,0.2,0.3,0.4,0.5])
    i=0
    om=np.array([])
    ar=np.array([])
    while(i!=5):
        w_sub0=18.55
        omega=np.array(np.random.randint(0,w_sub0*2))
        Arm=np.array([C(4300,12.5,w_sub0,omega,CoeR[i])])
        om=np.append(om,omega)
        ar=np.append(ar,Arm)
        plt.plot(om / w_sub0, ar, linewidth=2, color='red')
        i=i+1
    plt.title("Movimiento Armónico Forzado")
    plt.xlabel("Omega/W", color='red')
    plt.ylabel('Amplitud', color='red')
    plt.show()

Graficar()