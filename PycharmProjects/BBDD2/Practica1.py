from tkinter import *
from tkinter import messagebox
import sqlite3

#Funciones
def Salir():
    S=messagebox.askokcancel("Salir", "Confirme salida del programa")
    if(S==True):
        Root.destroy()
def Conectar():
    Conexion=sqlite3.connect("InformacionUsuarios")
    Cursor=Conexion.cursor()
    try:
        Cursor.execute('''
        CREATE TABLE Usuarios(
        usua_id numeric not null,
        usua_nombres VARCHAR(50) not null,
        usua_apellidos VARCHAR(50),
        usua_telefono numeric,
        usua_direccion varchar(50),
        usua_municipio varchar(50),
        usua_vereda varchar(50))
        ''')
        messagebox.showinfo("BBDD", "Base de datos creada correctamente")
    except:
        messagebox.showwarning("¡Error!","Base de datos ya existe")
    Conexion.close()

def LimpiarCampos():
    MiID.set("")
    MiNombres.set("")
    MiApellidos.set("")
    MiTelefono.set("")
    MiDireccion.set("")
    MiMunicipio.set("")
    MiVereda.set("")
def CREATE():
    Conexion = sqlite3.connect("InformacionUsuarios")
    Cursor = Conexion.cursor()
    '''Cursor.execute("INSERT INTO Usuarios VALUES('MiID.get()+
    " ' , '"+MiNombres.get()+
    " ' , ' "+MiApellidos.get()+
    " ' , ' "+MiTelefono.get()+
    " ' , ' "+MiDireccion.get()+
    " ' , ' "+MiMunicipio.get()+
    " ' , ' "+MiVereda.get())")'''
    #Consulta parametrizada
    Datos=MiID.get(),MiNombres.get(),MiApellidos.get(),MiTelefono.get(),MiDireccion.get(),MiMunicipio.get(),MiVereda()
    Cursor.execute("INSERT INTO Usuarios VALUES(?,?,?,?,?,?,?)",(Datos))
    Conexion.commit()
    messagebox.showinfo("CREATE","Datos ingresados correctamente")
def READ():
    Conexion=sqlite3.connect("InformacionUsuarios")
    Cursor=Conexion.cursor()
    Cursor.execute("SELECT * FROM Usuarios WHERE Id="+MiID.get())
    Lectura=Cursor.fetchall()
    for i in Lectura:
        MiID.set(i[0])
        MiNombres.set(i[1])
        MiApellidos.set(i[2])
        MiTelefono.set(i[3])
        MiDireccion.set(i[4])
        MiMunicipio.set(i[5])
        MiVereda.set(i[6])
    Conexion.commit()

def UPDATE():
    Conexion = sqlite3.connect("InformacionUsuarios")
    Cursor = Conexion.cursor()
    '''Cursor.execute("UPDATE Usuarios SET 
    Id=' "+MiID.get()+
    " ', Nombres=' "+MiNombres.get()+
    " ', Apellidos=' "+MiApellidos.get()+
    " ', Telefono=' "+MiTelefono.get()+
    " ', Direccion=' "+MiDireccion.get()+
    " ', Municipio=' "+MiMunicipio.get()+
    " ', Vereda=' "+MiVereda.get()+
    " ' WHERE Id= "+MiID.get())'''
    #Consulta parametrizada
    Datos =MiID.get(),MiNombres.get(),MiApellidos.get(),MiTelefono.get(),MiDireccion.get(),MiMunicipio.gD
    Cursor.execute("UPDATE Usuarios SET "
                   "Id=?, Nombres=?,"
                   "Apellidos=?,"
                   "Telefono=?,"
                   "Direccion=?,"
                   "Municipio=?,"
                   "Vereda=? WHERE Id= "+MiID.get(),(Datos))
    Conexion.commit()
    messagebox.showinfo("Base de datos","Registro insertados con exito")

def DELETE():
    Conexion=sqlite3.connect("InformacionUsuarios")
    Cursor=Conexion.cursor()
    Cursor.execute("DELETE FROM Usuarios WHERE Id="+ MiID.get())
    Conexion.commit()
    messagebox.showinfo("Base de datos", "Registro eliminado con exito")
Root=Tk()
Root.title("Interfaz CRUD")
Root.iconbitmap("J.ico")
#Menu
BarraM=Menu(Root)
Root.config(menu=BarraM,width=400,height=300,bg="red")
BBDD=Menu(BarraM,tearoff=0)
BBDD.add_command(label="Conectar",command=Conectar)
BBDD.add_command(label="Salir",command=Salir)
Borrar=Menu(BarraM,tearoff=0)
Borrar.add_command(label="Borrar campos",command=LimpiarCampos)
CRUD=Menu(BarraM,tearoff=0)
CRUD.add_command(label="Crear",command=CREATE)
CRUD.add_command(label="Leer",command=READ)
CRUD.add_command(label="Actualizar",command=UPDATE)
CRUD.add_command(label="Borrar",command=DELETE)
Ayuda=Menu(BarraM,tearoff=0)
BarraM.add_cascade(label="BBDD",menu=BBDD)
BarraM.add_cascade(label="Borrar",menu=Borrar)
BarraM.add_cascade(label="CRUD",menu=CRUD)
BarraM.add_cascade(label="Ayuda",menu=Ayuda)
#FRAME
MiFrame=Frame(Root,width=500,height=400)
MiFrame.pack()

Id=Label(MiFrame,text="Cedula")
Id.grid(row=0,column=0,padx=20,pady=20)
Nombres=Label(MiFrame,text="Nombres")
Nombres.grid(row=1,column=0,padx=20,pady=20)
Apellidos=Label(MiFrame,text="Apellidos")
Apellidos.grid(row=2,column=0,padx=20,pady=20)
Telefono=Label(MiFrame,text="Telefono")
Telefono.grid(row=3,column=0,padx=10,pady=10)
Direccion=Label(MiFrame,text="Direccion")
Direccion.grid(row=4,column=0,padx=20,pady=20)
Municipio=Label(MiFrame,text="Municipio")
Municipio.grid(row=5,column=0,padx=20,pady=20)
Vereda=Label(MiFrame,text="Vereda")
Vereda.grid(row=6,column=0,padx=20,pady=20)

#Botones
MiFrame2=Frame(Root)
MiFrame2.pack()
Create=Button(MiFrame2,text="Create",command=CREATE)
Create.grid(row=0,column=0,padx=15,pady=8)
Read=Button(MiFrame2,text="Read",command=READ)
Read.grid(row=0,column=1,padx=15,pady=8)
Update=Button(MiFrame2,text="Update",command=UPDATE)
Update.grid(row=0,column=2,padx=15,pady=8)
Delete=Button(MiFrame2,text="Delete",command=DELETE)
Delete.grid(row=0,column=3,padx=15,pady=8)

#Cuadro de texto
MiID=StringVar()
MiNombres=StringVar()
MiApellidos=StringVar()
MiTelefono=StringVar()
MiDireccion=StringVar()
MiMunicipio=StringVar()
MiVereda=StringVar()

CID=Entry(MiFrame,textvariable=MiID)
CID.grid(row=0,column=1)
CNombres=Entry(MiFrame,textvariable=MiNombres)
CNombres.grid(row=1,column=1)
CApellidos=Entry(MiFrame,textvariable=MiApellidos)
CApellidos.grid(row=2,column=1)
CTelefono=Entry(MiFrame,textvariable=MiTelefono)
CTelefono.grid(row=3,column=1)
CDireccion=Entry(MiFrame,textvariable=MiDireccion)
CDireccion.grid(row=4,column=1)
CMunicipio=Entry(MiFrame,textvariable=MiMunicipio)
CMunicipio.grid(row=5,column=1)
CVereda=Entry(MiFrame,textvariable=MiVereda)
CVereda.grid(row=6,column=1)

Root.mainloop()