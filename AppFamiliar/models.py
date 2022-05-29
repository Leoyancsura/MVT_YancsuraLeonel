from django.db import models
import uuid #Libreria de generador de id.

# Create your models here.
class Familiar(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key=True, max_length=50)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()   
    profesion = models.CharField(max_length=30)
    direccion = models.CharField(max_length=40)