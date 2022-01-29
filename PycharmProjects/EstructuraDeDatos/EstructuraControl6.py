RaizD=int(input("Digite un numero: "))
def RaizDigital(RaizD):
    Aux=0
    while(RaizD!=0):
        Aux+=RaizD%10
        RaizD=int(RaizD/10)
    if(Aux<10):
        if(print(Aux)==None):
            exit()
    else:
        print(RaizDigital(Aux))
RaizDigital(RaizD)