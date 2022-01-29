from tkinter import *
Root=Tk()
Root.title("Interfaz grafica")
Frame=Frame(Root,width=500,height=400)
Frame.pack()
Imagen=PhotoImage(file="Imagen.png")
#Label=Label(Frame,text="Hola Jaider Ivan",fg="red",font=("Comic Sans Ms",18))
#Label.place(x=200,y=200)
Label(Frame,image=Imagen).place(x=200,y=100) #Abreviatura
Root.mainloop()