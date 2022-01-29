import pickle
Vec=["Jaider","Misael","Milena","Camilo"]
FicheroB=open("ListaN","wb")#wb Escritura binaria
pickle.dump(Vec,FicheroB)
FicheroB.close()
del(FicheroB)
FicheroB=open("ListaN","rb")#rb Lectura Binaria
Vec2=pickle.load(FicheroB)
print(Vec2)