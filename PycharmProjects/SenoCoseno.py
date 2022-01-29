import math
def Factorial(X):
    F=1
    while X>1:
        F*=X
        X-=1
    return F
def Seno(X):
    R=0
    Rta=0

    while(R<15):
        Rta+=((-1)**R/Factorial(2*R+1))*(Grado_A_Radianes(X)**(2*R+1))
        R+=1
    return Rta

def Grado_A_Radianes(X):
    R=X*(math.pi/180)
    return R

print(Seno(90))