class Vehiculos():
    def __init__(self,Marca,Modelo):
        self.Marca=Marca
        self.Modelo=Modelo
        self.Estado=False
        self.Acelera=False
        self.Frenado=False
    def Arrancar(self):
        self.Estado=True
    def Aceleracion(self):
        self.Acelera=True
    def Frenar(self):
        self.Frenado=True
    def Info(self):
        print("Marca: ",self.Marca,"\nModelo: ",self.Modelo,
              "\nAcelerando: ",self.Acelera,"\nFrenando: ",self.Frenado)
class VehiculosE():
    def __init__(self,Marca,Modelo):
        super().__init__(Marca,Modelo)
        self.Autonomia=100
    def Carga(self):
        print("Cargando")
class Moto(Vehiculos):
    __Caballito="No"
    def CaballitoM(self):
        __Caballito="Estoy haciendo caballito"
    def Info(self):#La sobrescritura se realiza automaticamente
        print("Marca: ",self.Marca,"\nModelo: ",self.Modelo,
              "\nAcelerando: ",self.Acelera,"\nFrenando: ",self.Frenado,"EstadoCaballio"
              ,self.__Caballito)
class Camion(Vehiculos):
    def Carga(self,Carga):
        self.Cargado=Carga
        if(self.Cargado):
            return "Cargado"
        else:
            return "Vacio"
class BiciE(VehiculosE,Vehiculos):#Herencia multiple, Contructor de la primera clase
    pass
Motoo=Moto("Buga","Shimba")
Motoo.Info()
Motoo.CaballitoM()
Camioon=Camion("Duro","Platano")
Camioon.Info()
print(Camioon.Carga(True))
Bicicleta=BiciE("Ferrucho","SDFGD")#Constructor con clase super
Bicicleta.Info()
print(Bicicleta.Autonomia)