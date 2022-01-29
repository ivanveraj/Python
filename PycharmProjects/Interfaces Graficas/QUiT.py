import tkinter as tk
class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.Creawidgets()
    def Creawidgets(self):
        self.Boton=tk.Button(self)
        self.Boton["text"]="Hola mundo\n(click me)"
        self.Boton["command"]=self.DecirHola
        self.Boton.pack(side="top")
        self.Salir=tk.Button(self, text="Salir", fg="red",
                command=self.master.destroy)
        self.Salir.pack(side="bottom")
    def DecirHola(self):
        print("Hola Jaider")
Root=tk.Tk()
App=App(master=Root)
App.mainloop()