from django.db import models
import email

class Empleados(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()

class Vacantes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    mail = models.EmailField()
    dni = models.IntegerField()

class Clientes(models.Model):

    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()



    
# Create your models here.
