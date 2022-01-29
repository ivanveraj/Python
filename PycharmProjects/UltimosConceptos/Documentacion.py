import doctest
def AreaT(B,H):
    '''Esta funcion realiza el calculo el area de un triangulo dado
    >>> AreaT(5,6)
    15.0
    >>> AreaT(5,6)#ERROR creado
    12.0
    '''
    return "El area del triangulo es",(B*H)/2
doctest.testmod()