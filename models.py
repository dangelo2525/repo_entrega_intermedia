from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada= models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada} "
    
class Alumno (models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    nacimiento = models.DateField()
    

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    

class Profesor (models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    nacimiento = models.DateField()
    





    
    