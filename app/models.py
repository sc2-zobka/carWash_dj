from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator


# Create your models here.


# Servicio: simple, gold, premiun -> (Producto)
class Servicio(models.Model):

    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="servicios", null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicio"


class Slider(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="slider", null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"


class Galeria(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="galeria", null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galeria"


# Insumo must be handled outside of Django Admin


'''class Insumo(models.Model):
    nombre = models.CharField(validators=[MinLengthValidator(
                                limit_value=3,
                                message='Minimo 3 carácteres!')],
                              max_length=120)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="insumo", null=True)
    descripcion = models.TextField(validators=[MinLengthValidator(
                                limit_value=3,
                                message='Minimo 3 carácteres!')],
                              max_length=200)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
'''
