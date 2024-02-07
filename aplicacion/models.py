from django.db import models

# Create your models here.

class Planta(models.Model):
    nombre = models.CharField(max_length=50)
    ambiente = models.CharField(max_length=50)
    riego = models.CharField(max_length=50)
    iluminacion = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.nombre}"

class Maceta(models.Model):
    material = models.CharField(max_length=50)
    forma = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"Maceta de {self.material}"

class Fertilizante(models.Model):
    nombre = models.CharField(max_length=50)
    nutrientes = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    precauciones = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.nombre}"
    