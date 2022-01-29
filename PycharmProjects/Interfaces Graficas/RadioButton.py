from tkinter import *
Root=Tk()
Var=IntVar()
def Imprimir():
    if(Var.get()==1):
        Etiqueta.config(text="Elegido masculino")
    else:
        Etiqueta.config(text="Elegido femenino")
Label(Root,text="Genero:").pack()
Boton1=Radiobutton(Root,text="Masculino",variable=Var,value=1,command=Imprimir).pack()
Boton2=Radiobutton(Root,text="Femenino",variable=Var,value=2,command=Imprimir).pack()
Etiqueta=Label(Root)
Etiqueta.pack()
Root.mainloop()