from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Novela(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    precio = models.FloatField()
    imagen_libro = models.ImageField(upload_to="imagenes_libros", null=True)
    

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    


class Manga(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    precio = models.FloatField()
    imagen_libro = models.ImageField(upload_to="imagenes_libros", null=True)
    

    def __str__(self):
     return f"{self.titulo} - {self.autor}"
    

class Comics(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    precio = models.FloatField()
    imagen_libro = models.ImageField(upload_to="imagenes_libros", null=True)

    def __str__(self):
     return f"{self.titulo} - {self.autor}"



