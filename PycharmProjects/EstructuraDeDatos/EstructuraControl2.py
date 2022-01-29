Sexo=int(input("Digite su sexo \n[1]Masculino\n[2]Femenino\n"))
if(Sexo==1 or Sexo==2):
    Edad=int(input("Digite su edad\n"))
    if(Sexo==1):
        Numpulsaciones=(210-Edad)/10
    else:
        Numpulsaciones=(220-Edad)/10
    print(Numpulsaciones)
else:
    print("Error")
