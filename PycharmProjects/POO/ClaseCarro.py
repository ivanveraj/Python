class Carro():
    def __init__(self):#Constructor palabra init
        self.LargoC=250
        self.AnchoC=120
        self.__Ruedas=4#private  guiones bajos
        self.Encendido=False
    def Informacion(self):
        print("Largo del chasis",self.LargoC,"\nAncho del chasis",self.AnchoC,"\n"
                "Total ruedas",self.__Ruedas,"\nEstado: ",self.Encendido)
    def Encender(self):
        self.Encendido=True
        print("Estado del coche: ",self.Encendido)
    def Estado(self):
        if(self.Encendido):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    def Verificacion(self):
        print("Realizando verificacion general")
        
Carro1=Carro()
Carro1.Informacion()
Carro1.Encender()
print(Carro1.Estado())
print("Segundo objeto")
Carro2=Carro()#Segunda instancia de la clase
Carro2.AnchoC=150#Set modificacion del constructor
Carro2.Informacion()
print(Carro2.Estado())