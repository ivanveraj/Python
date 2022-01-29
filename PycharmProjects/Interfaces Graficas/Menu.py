from tkinter import *
from tkinter import messagebox#Ventanas emergentes
def Abrir():
    messagebox.showinfo("Abrir archivo o proyecto","Aplicaciones")
def Aviso():
    messagebox.showerror("Producto licencia", "Licencia vencida")
def SalirApp():
    #S=messagebox.askquestion("Salir","Confirmar")#Devuelve yes o no
    S=messagebox.askokcancel("Salir", "Confirmar")
    if(S==True):
        Root.destroy()
def CerrarArchivo():
    S=messagebox.askretrycancel("Reintentar","No es posible cerrar el documetno")
    if (S==False):#Devuelve True o False
        Root.destroy()
Root=Tk()
BarraM=Menu(Root)
Root.config(menu=BarraM,width=400,height=300)
#File
FileM=Menu(BarraM,tearoff=0)
FileM.add_command(label="Nuevo proyecto")
FileM.add_command(label="Nuevo")
FileM.add_command(label="Abrir",command=Abrir)
FileM.add_separator()
FileM.add_command(label="Cerrar",command=CerrarArchivo)
FileM.add_command(label="Salir",command=SalirApp)

EditM=Menu(BarraM,tearoff=0)
EditM.add_command(label="Copiar")
EditM.add_command(label="Cortar")
EditM.add_command(label="Pegar")

ViewM=Menu(BarraM,tearoff=0)
ViewM.add_command(label="Apariencia")

NavigateM=Menu(BarraM,tearoff=0)
NavigateM.add_command(label="Buscar")
NavigateM.add_command(label="Archivo")
NavigateM.add_command(label="Clase")
NavigateM.add_command(label="Licencia",command=Aviso)


BarraM.add_cascade(label="File",menu=FileM)
BarraM.add_cascade(label="Edit",menu=EditM)
BarraM.add_cascade(label="View",menu=ViewM)
BarraM.add_cascade(label="Navigate",menu=NavigateM)


Root.mainloop()