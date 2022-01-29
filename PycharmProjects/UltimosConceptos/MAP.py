class Empleado:
    def __init__(self,N,C,S):
        self.Nombre=N
        self.Cargo=C
        self.Salario=S
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.Nombre,self.Cargo,self.Salario)

ListaEmpleados=[
Empleado("Ivan","Dirrector",500),
Empleado("Jaider","CEO",800),
Empleado("Mile","Dirrectora",500),
Empleado("Ramon","Empleado",200),
]
def Comision(E):
    if(E.Salario<=200):
        E.Salario=E.Salario*1.03
    return(E)

ListaEmpleadosMAP=map(Comision,ListaEmpleados)
for i in ListaEmpleadosMAP:
    print(i)

