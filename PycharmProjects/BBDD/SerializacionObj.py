import pickle
class Vehiculo():
    def __init__(self, Marca, Modelo):
            self.Marca = Marca
            self.Modelo = Modelo
            self.Estado = False
            self.Acelera = False
            self.Frenado = False
    def Arrancar(self):
            self.Estado = True
    def Aceleracion(self):
            self.Acelera = True
    def Frenar(self):
            self.Frenado = True
    def Info(self):
            print("Marca: ", self.Marca, "\nModelo: ", self.Modelo,
                  "\nAcelerando: ", self.Acelera, "\nFrenando: ", self.Frenado)
C=Vehiculo("Mazda","RCFG")
C2=Vehiculo("Renault","FGHD")
C3=Vehiculo("Buga","RTYF")
Coches=[C,C2,C3]
FicheroB=open("Coches","wb")
pickle.dump(Coches,FicheroB)
FicheroB.close()
del(FicheroB)
FicheroBA=open("Coches","rb")
MisCoches=pickle.load(FicheroBA)
FicheroBA.close()
for i in MisCoches:
    print(i.Info())