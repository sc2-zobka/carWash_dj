from django.urls import path
from .views import home, contacto, mision


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('mision/', mision, name="mision"),
]
