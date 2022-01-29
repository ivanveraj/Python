from tkinter import *

Root=Tk()
P=IntVar()
C=IntVar()
B=IntVar()
def Opciones():
    Op=""
    if(P.get()==1):
        Op+="Pamplona"
    if(C.get()==1):
        Op += "Cucuta"
    if (B.get()==1):
        Op+="Bucaramanga"
    Texto.config(text=Op)
Imagen=PhotoImage(file="Imagen.png")
Label(Root,image=Imagen).pack()
Frame=Frame(Root)
Frame.pack()
Label(Frame,text="Elige Destino").pack()
Checkbutton(Frame,text="Pamplona",variable=P,onvalue=1,offvalue=0,command=Opciones).pack()
Checkbutton(Frame,text="Cucuta",variable=C,onvalue=1,offvalue=0,command=Opciones).pack()
Checkbutton(Frame,text="Bucaramanga",variable=B,onvalue=1,offvalue=0,command=Opciones).pack()
Texto=Label(Frame)
Texto.pack()
Root.mainloop()