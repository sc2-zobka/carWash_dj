from django.db import models

# Create your models here.
class Slider(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="slider", null=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="servicio", null=True)

    def __str__(self):
        return self.nombre

class Insumo(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="insumo", null=True, blank=True)
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="galeria", null=True)

    def __str__(self):
        return self.nombre

class Mision(models.Model):
    nombre = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Vision(models.Model):
    nombre = models.CharField(max_length=30)
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre