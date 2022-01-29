'''def Par(N):
    if(N%2==0):
        return(True)

Num=[17,23,56,67,437,256,775,42]
print(list(filter(Par,Num)))'''

'''Num=[17,23,56,67,437,256,775,42]
print(list(filter(lambda N:N%2==0,Num)))'''

class Empleado:
    def __init__(self,N,C,S):
        self.Nombre=N
        self.Cargo=C
        self.Salario=S
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de ${}".format(self.Nombre,self.Cargo,self.Salario)

ListaEmpleados=[
Empleado("Ivan","Dirrector",50000),
Empleado("Jaider","CEO",80000),
Empleado("Mile","Dirrectora",50000),
Empleado("Ramon","Empleado",20000),
]
SalariosAltos=filter(lambda empleado:empleado.Salario>49000,ListaEmpleados)
for i in SalariosAltos:
    print(i)