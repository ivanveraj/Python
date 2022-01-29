import pandas as pd

def funcion_promedioDic(Serie):
    i=0
    Suma=0
    while i<len(Serie):
        Suma+=Serie[i]['Vacunados']
        i+=1
    promedio=Suma/len(Serie)
    return int(promedio)
def funcion_promedio(lista):
    i=0
    Suma=0
    while i<len(lista):
        Suma+=lista[0]
        i+=1
    promedio=Suma/len(lista)
    return int(promedio)
Dicc=pd.Series([{'Dep':'Arauca','Vacunados':535453},
                {'Dep':'Antioquia','Vacunados':535336773},
                {'Dep':'Nariño','Vacunados':198988867867},
                {'Dep':'Risaralda','Vacunados':876777},
                {'Dep':'Quindio','Vacunados':9887776},
                {'Dep':'Putumayo','Vacunados':1235678},
                {'Dep':'Norte de Santander','Vacunados':66578876},
                {'Dep':'Santander','Vacunados':653531},
                {'Dep':'Amazonas','Vacunados':7765656},
                {'Dep':'La Guajira','Vacunados':88766632},
                {'Dep':'Cesar','Vacunados':12135189},
                {'Dep':'Huila','Vacunados':5555544},
                {'Dep':'Boyaca"','Vacunados':4444432},
                {'Dep':'Casanare','Vacunados':222222}])
NVacunados= pd.Series([123,333,556,778,5,666,43,32,3,3232,32,324,324,32,253553])
print(Dicc)
print("El promedio de vacunas aplicadas en los 15 departamentos fue: ",funcion_promedioDic(Dicc))
print("Lista con la cantidad de vacunados")
Lista=[123123,43221,432118,53666,654232,5655488,856763523,1432432,235367,253232531,665757563]
print(Lista)
print("El promedio de vacunados fue: ",funcion_promedio(Lista))
