Codigo=int(input("Digite el codigo de la votacion del pasado domingo "))
Aux=0
if(Codigo>=1100 and Codigo<=9999):
    D1=int(Codigo/1000)
    D2=int((Codigo/100)%10)
    D3=int(Codigo % 100)
    if(D1==1):
        print("Partido:Liberal")
    if(D1==2):
        print("Partido:Conservador")
    if (D1==3):
        print("Partido: de la U")
    if (D1==4):
        print("Partido:ANSI")
    if (D1==5):
        print("Partido:Rey")
    if (D1==6):
        print("Partido:Polo democratico")
    if (D1==7):
        print("Partido:Radical")
    if (D1==8):
        print("Partido:Neoliberal")
    if (D1==9):
        print("Partido:Centro democratico")
    if(D2%2==0):
        print("Voto:Camara")
    else:
        print("Voto:Senado")
    print("Numero de candidato:",D3)
else:
    print("Error codigo incorrecto")
