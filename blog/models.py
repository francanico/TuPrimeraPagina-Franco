from django.db import models

# Create your models here.
class Poliza(models.Model):
    nombre = models.CharField(max_length= 50)
    precio = models.DecimalField(max_digits= 15, decimal_places=2)
    categoria= models.CharField(max_length=50)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    registro = models.IntegerField()

class Auto(models.Model):
    marca= models.CharField(max_length=50)
    modelo=models.CharField(max_length=40)
    color= models.CharField(max_length=20)
    placa= models.CharField(max_length=30)
    kilometraje=models.IntegerField()