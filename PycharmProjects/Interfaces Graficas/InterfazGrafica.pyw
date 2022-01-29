from tkinter import *
Raiz=Tk()#Inicia
Raiz.title("Interfaz grafica")#Titulo de la ventana
Raiz.iconbitmap("J.ico")#Icono
#Raiz.geometry("500x500")#Tamaño de la ventana
#Raiz.resizable(1,1)#Booleanos o Uno y ceros Width,Height
Raiz.config(bg="grey")#Fondo de pantalla
Frame=Frame()
#Frame.pack(side="right", anchor="s")#anchor no tiene necesidad de utilizar side
Frame.pack(fill="y", expand=True)#Expansion del Frame
Frame.config(width="500",height="500")#La raiz se adapta al Frame
Frame.config(bg="red")
Frame.config(bd="35")#Tamaño del borde
Frame.config(relief="groove")#Sunken
Frame.config(cursor="hand2")
Raiz.mainloop()#Bucle infinito