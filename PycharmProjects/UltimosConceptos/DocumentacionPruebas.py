import math
import doctest
def RaizC(Lista):
    '''La funcion devuelve una lista con la raiz cuadrada de los
    elementos numericos en otra lista
    >>> L=[]
    >>> for i in[4,9,16]:
    ...         L.append(i)
    >>> RaizC(L)
    [2.0, 3.0, 4.0]


    '''
    return [math.sqrt(N) for N in Lista]

doctest.testmod()
#print(RaizC([9,16,25,36]))