from tkinter import *
from tkinter import filedialog
Root=Tk()
def AbrirFichero():
    Fichero=filedialog.askopenfilename(title="Abrir ",initialdir="c:",filetypes=(("Fichero de Word","*.docx*"),
        ("Ficheros Imagenes","*.png*"),("Todos los ficheros","*.*")))#Ruta de inicio
    #filetypes recibe una tupla, filtro de busqueda
    print(Fichero)
def GuardarFichero():
    Fichero=filedialog.asksaveasfilename(title="Guardar ",initialdir="/",filetypes=(("Fichero de Word","*.docx*"),
        ("Ficheros Imagenes","*.png*"),("Todos los ficheros","*.*")))#Ruta de inicio
    #filetypes recibe una tupla, filtro de busqueda
    print(Fichero)
def AskFichero():
    Fichero=filedialog.askdirectory()
    print(Fichero)
Button(Root,text="Abrir Fichero",command=AbrirFichero).pack()
Button(Root,text="Guardar Fichero",command=GuardarFichero).pack()
Button(Root,text="Ask Fichero",command=AskFichero).pack()
Root.mainloop()