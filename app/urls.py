from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('insumos/', insumos, name="insumos"),
    path('modificar_insumo/<id>/', modificar_insumo, name="modificar_insumo"),
    path('eliminar_insumo/<id>/', eliminar, name="eliminar_insumo"),
    path('mision/', mision, name="mision"),
    path('registro/', registro, name="registro"),
]