from tkinter import *
Root=Tk()
Nombre=StringVar()
Frame=Frame(Root,width=500,height=500)
Frame.pack()
Frame.config(bg="grey")
LabelN=Label(Frame,text="Nombre")
LabelN.grid(row=0,column=0,sticky="w",padx=20,pady=20)
LabelA=Label(Frame,text="Apellido")
LabelA.grid(row=1,column=0,sticky="w",padx=20,pady=20)
LabelD=Label(Frame,text="Dirrecion")
LabelD.grid(row=2,column=0,sticky="w",padx=20,pady=20)
LabelP=Label(Frame,text="Contraseña")
LabelP.grid(row=3,column=0,sticky="w",padx=20,pady=20)
LabelC=Label(Frame,text="Comentarios")
LabelC.grid(row=4,column=0,sticky="w",padx=20,pady=20)

TextoC=Text(Frame,width=20, height=10)
TextoC.grid(row=4, column=1,padx=20,pady=20)

BarraD=Scrollbar(Frame,command=TextoC.yview)#Barra vertical
#BarraD=Scrollbar(Frame,command=TextoC.xview)#Barra horizontal
BarraD.grid(row=4,column=2,sticky="nswe")
TextoC.config(bg="green",bd=12,fg="white",yscrollcommand=BarraD.set)

CuadroN=Entry(Frame, textvariable=Nombre)
CuadroN.grid(row=0,column=1)
CuadroA=Entry(Frame)
CuadroA.grid(row=1,column=1)
CuadroD=Entry(Frame)
CuadroD.grid(row=2,column=1)
CuadroP=Entry(Frame)
CuadroP.config(show="*")
CuadroP.grid(row=3,column=1)
def PonerNombre():
    Nombre.set("Jaider Ivan Vera")

Boton=Button(Root,text="Enviar",command=PonerNombre)
Boton.pack()

Root.mainloop()