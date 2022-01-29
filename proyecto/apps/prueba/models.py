from django.db import models

# Create your models here.
class Persona(models.Model):
    cedula=models.IntegerField
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.FloatField()
    estatura=models.FloatField()

    def __str__(self):
        return self.nombre

class Animal(models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    dueno=models.ForeignKey(Persona, on_delete=models.RESTRICT)
