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


class Mision(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200, blank=True,
                                   help_text="Escriba un mensaje para\
                                   mostrar en la seccion de Mision\
                                   del sitio web")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Mision"
        verbose_name_plural = "Mision"


class Vision(models.Model):

    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=200, blank=True,
                                   help_text="Escriba un mensaje para\
                                   mostrar en la seccion de Vision\
                                   del sitio web")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Vision"
        verbose_name_plural = "Vision"


opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    opciones_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    recibir_ofertas = models.BooleanField(name="ofertas",
                                          help_text="Reciba nuestras ofertas\
                                              exclusivas!")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contacto"


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
