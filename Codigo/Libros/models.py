from django.db import models

# Create your models here.

class Novela(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    precio = models.FloatField()

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    


class Manga(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    precio = models.FloatField()

    def __str__(self):
     return f"{self.titulo} - {self.autor}"
    

class Comics(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    precio = models.FloatField()

    def __str__(self):
     return f"{self.titulo} - {self.autor}"
