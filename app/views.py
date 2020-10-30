from django.shortcuts import render
<<<<<<< HEAD
from .models import Servicio, Slider
=======
from .models import Servicio, Slider, Galeria
>>>>>>> feature/galeria-model

# Create your views here.


def home(request):
    # fetch all Servicios objects into a list[]
    servicios = Servicio.objects.all()
    fotos_slider = Slider.objects.all()

    fotos_slider = Slider.objects.all()

    # store into data{} all Servicio's objects
    # and render it to django template "Home"
    data = {
        'servicios': servicios,  # key:'servicios' could be any name
        'slider': fotos_slider
    }
    return render(request, 'app/home.html', data)  # data as a third param


def contacto(request):
    return render(request, 'app/contacto.html')


def mision(request):

    fotos_galeria = Galeria.objects.all()
    data = {
        'galeria': fotos_galeria
    }
    return render(request, 'app/mision.html', data)
