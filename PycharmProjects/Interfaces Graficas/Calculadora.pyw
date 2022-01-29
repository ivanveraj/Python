from tkinter import *
'''Pulsaciones'''
def NumeroPulsado(Numero):
    global Op,BorradoC
    if BorradoC!=False:
        Num.set(Numero)
        BorradoC=False
    else:
        Num.set(Num.get()+Numero)
'''Operaciones Basicas'''
def FuncionSuma(S):
    global Op,Resultado,BorradoC,ContadorG
    Op="Suma"
    Resultado+=float(S)
    BorradoC=True
    Num.set(Resultado)
def FuncionResta(R):
    global Op,Resultado,Aux,ContadorR,BorradoC,ContadorG
    if ContadorR==0:
        Aux=float(R)
        Resultado=Aux
    else:
        if ContadorR==1:
            Resultado=Aux-float(R)
        else:
            Resultado=float(Resultado)-float(R)
    Op="Resta"
    Num.set(Resultado)
    ContadorR+=1
    ContadorG+=1
    BorradoC=True
def FuncionMultiplicacion(M):
    global Op,Resultado,Aux,ContadorM,BorradoC,ContadorG
    if(ContadorM==0):
        Aux=float(M)
        Resultado=Aux
    else:
        if(ContadorM==1):
            Resultado=Aux*float(M)
        else:
            Resultado=float(Resultado)*float(M)
        Num.set(Resultado)
        Resultado=Num.get()
    Op="Multiplicacion"
    ContadorM+=1
    ContadorG += 1
    BorradoC=True
def FuncionDivision(D):
    global Op,Resultado,Aux,ContadorD,BorradoC,ContadorG
    if(ContadorD==0):
        Aux=float(D)
        Resultado=Aux
    else:
        if ContadorD==1:
            Resultado=Aux/float(D)
        else:
            Resultado=float(Resultado)/float(D)
        Num.set(Resultado)
        Resultado=Num.get()
    ContadorD+=1
    ContadorG+=1
    Op="Division"
    BorradoC=True
def FuncionC():
    Num.set("")
def Borrar(N):
    Auxiliar=int(float(N)/10)
    Num.set(Auxiliar)
'''def FuncionCE():
    global Aux
    if(ContadorG==0):
        Num.set("")
    else:
        Aux=Num.get()
        Num.set("")'''
def FuncionIgual():
    global Resultado,Op,ContadorG,ContadorD,ContadorM,ContadorR
    print(Op)
    if Op=="Suma":
        Num.set(Resultado+float(Num.get()))
        Resultado=0
        ContadorG=0
    elif Op=="Resta":
        Num.set(Resultado-float(Num.get()))
        Resultado = 0
        ContadorG = 0
        ContadorR=0
    elif Op=="Multiplicacion":
        Num.set(Resultado*float(Num.get()))
        Resultado = 0
        ContadorG = 0
        ContadorM=0
    elif Op=="Division":
        Num.set(Resultado/float(Num.get()))
        Resultado = 0
        ContadorG = 0
        ContadorD=0
Root=Tk()
Root.title("Calculadora")
Root.iconbitmap("J.ico")
Root.config(bg="#D9120F")
Frame=Frame(Root)
Frame.pack(expand=False)
Frame.config(bg="#06BFC5",bd="15",relief="groove")
Op=""
Resultado=0
ContadorR=0
ContadorM=0
ContadorD=0
ContadorG=0
Aux=0
Oscuro=0
BorradoC=False
'''Pantalla'''
Num=StringVar()
if(Num.get()==0):
    Num.set("")
Pantalla=Entry(Frame, textvariable=Num,width=40)
Pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4,ipady=8)
Pantalla.config(bg="#FFFFFF",fg="#000000",justify="right",font=("Comic Sans Ms",11))
'''Fila0'''
BotonCE=Button(Frame,text="CE",width=7,height=2)
BotonCE.grid(row=2,column=1,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonCE.config(font=("Comic Sans Ms",11))
BotonC=Button(Frame,text="C",width=7,height=2,command=lambda:FuncionC())
BotonC.grid(row=2,column=2,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonC.config(font=("Comic Sans Ms",11))
BotonB=Button(Frame,text="<--",width=7,height=2,command=lambda:Borrar(Num.get()))
BotonB.grid(row=2,column=3,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonB.config(font=("Comic Sans Ms",11))
BotonD=Button(Frame,text="/",width=7,height=2,command=lambda:FuncionDivision(Num.get()))
BotonD.grid(row=2,column=4,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonD.config(font=("Comic Sans Ms",11))
'''Fila1'''
Boton7=Button(Frame,text="7",width=7,height=2, command=lambda:NumeroPulsado("7"))
Boton7.grid(row=3,column=1,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton7.config(font=("Comic Sans Ms",11))
Boton8=Button(Frame,text="8",width=7,height=2, command=lambda:NumeroPulsado("8"))
Boton8.grid(row=3,column=2,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton8.config(font=("Comic Sans Ms",11))
Boton9=Button(Frame,text="9",width=7,height=2, command=lambda:NumeroPulsado("9"))
Boton9.grid(row=3,column=3,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton9.config(font=("Comic Sans Ms",11))
BotonM=Button(Frame,text="X",width=7,height=2,command=lambda:FuncionMultiplicacion(Num.get()))
BotonM.grid(row=3,column=4,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonM.config(font=("Comic Sans Ms",11))
'''Fila2'''
Boton4=Button(Frame,text="4",width=7,height=2, command=lambda:NumeroPulsado("4"))
Boton4.grid(row=4,column=1,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton4.config(font=("Comic Sans Ms",11))
Boton5=Button(Frame,text="5",width=7,height=2, command=lambda:NumeroPulsado("5"))
Boton5.grid(row=4,column=2,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton5.config(font=("Comic Sans Ms",11))
Boton6=Button(Frame,text="6",width=7,height=2, command=lambda:NumeroPulsado("6"))
Boton6.grid(row=4,column=3,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton6.config(font=("Comic Sans Ms",11))
BotonMe=Button(Frame,text="-",width=7,height=2,command=lambda:FuncionResta(Num.get()))
BotonMe.grid(row=4,column=4,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonMe.config(font=("Comic Sans Ms",11))
'''Fila3'''
Boton1=Button(Frame,text="1",width=7,height=2, command=lambda:NumeroPulsado("1"))
Boton1.grid(row=5,column=1,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton1.config(font=("Comic Sans Ms",11))
Boton2=Button(Frame,text="2",width=7,height=2, command=lambda:NumeroPulsado("2"))
Boton2.grid(row=5,column=2,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton2.config(font=("Comic Sans Ms",11))
Boton3=Button(Frame,text="3",width=7,height=2, command=lambda:NumeroPulsado("3"))
Boton3.grid(row=5,column=3,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton3.config(font=("Comic Sans Ms",11))
BotonS=Button(Frame,text="+",width=7,height=2,command=lambda:FuncionSuma(Num.get()))
BotonS.grid(row=5,column=4,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonS.config(font=("Comic Sans Ms",11))
'''Fila4'''
Boton0=Button(Frame,text="0",width=7,height=2, command=lambda:NumeroPulsado("0"))
Boton0.grid(row=6,column=1,padx=5,pady=5,ipady=0.2,ipadx=0.2)
Boton0.config(font=("Comic Sans Ms",11))
BotonD0=Button(Frame,text="00",width=7,height=2,command=lambda:NumeroPulsado("00"))
BotonD0.grid(row=6,column=2,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonD0.config(font=("Comic Sans Ms",11))
BotonComa=Button(Frame,text=",",width=7,height=2,command=lambda:NumeroPulsado("."))
BotonComa.grid(row=6,column=3,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonComa.config(font=("Comic Sans Ms",11))
BotonI=Button(Frame,text="=",width=7,height=2,command=lambda:FuncionIgual())
BotonI.grid(row=6,column=4,padx=5,pady=5,ipady=0.2,ipadx=0.2)
BotonI.config(font=("Comic Sans Ms",11))
def ModoOscuro():
    global Oscuro
    if(Oscuro==0):
        Frame.config(bg="#000000", bd="15", relief="groove")
        Pantalla.config(bg="#FFFFFF", fg="#000000", justify="right")
        TemaOscuro=Button(Frame, text="TEMA CLARO", width=14, height=1, command=lambda: ModoOscuro())
        TemaOscuro.grid(row=7, column=0, columnspan=7,padx=0,pady=5,ipady=0.2,ipadx=0.2)
        TemaOscuro.config(font=("Comic Sans Ms", 11))
        Oscuro=1
    else:
        Frame.config(bg="#06BFC5",bd="15",relief="groove")
        Pantalla.config(bg="#FFFFFF", fg="#000000", justify="right")
        TemaOscuro=Button(Frame, text="TEMA CLARO", width=14, height=1, command=lambda: ModoOscuro())
        TemaOscuro.grid(row=7, column=0, columnspan=7,padx=0,pady=5,ipady=0.2,ipadx=0.2)
        TemaOscuro.config(font=("Comic Sans Ms", 11))
        Oscuro=0
TemaOscuro=Button(Frame,text="TEMA OSCURO",width=14,height=1,command=lambda:ModoOscuro())
TemaOscuro.grid(row=7,column=0,columnspan=7,padx=0,pady=5,ipady=0.2,ipadx=0.2)
TemaOscuro.config(font=("Comic Sans Ms",11))
Root.mainloop()