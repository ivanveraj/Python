import pickle
class Persona():
    def __init__(self,Nombre,Genero,Edad):
        self.Nombre=Nombre
        self.Genero=Genero
        self.Edad=Edad
        print("Se ha creado correctamente")
    def __str__(self):
        return "{}{}{}".format(self.Nombre,self.Genero,self.Edad)
class ListaP():
    Personas=[]
    def __init__(self):
        ListaPer=open("FicheroExterno","ab+")#ab+ Agregar informacion Binaria
        ListaPer.seek(0)
        try:
            self.Personas=pickle.load(ListaPer)
            print("Se cargaron ",len(Persona)," personas")
        except:
            print("Fichero vacio")
        finally:
            ListaPer.close()
            del(ListaPer)
    def Agregar(self,P):
        self.Personas.append(P)
        self.GuardarFichero()
    def Mostrar(self):
        for i in self.Personas:
            print(i)
    def GuardarFichero(self):
        ListaP=open("FicheroExterno","wb")
        pickle.dump(self.Personas,ListaP)
        ListaP.close()
        del(ListaP)
    def MostrarFichero(self):
        print("Info")
        for i in self.Personas:
            print(i)
L=ListaP()
P=Persona("Alejo","Masculino","14")
P2=Persona("Ivan","Masculino","17")
P3=Persona("RR","Femenino","22")
L.Agregar(P)
L.Agregar(P2)
L.Agregar(P3)
L.MostrarFichero()
