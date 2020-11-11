from django.shortcuts import render
from .models import Servicio, Slider, Galeria, Mision, \
    Vision, Contacto
from .forms import ContactoForm

# Create your views here.


def home(request):
    # fetch all Servicios objects into a list[]
    servicios = Servicio.objects.all()
    fotos_slider = Slider.objects.all()

    # store into data{} all Servicio's objects
    # and render it to django template "Home"
    data = {
        'servicios': servicios,  # key:'servicios' could be any name
        'slider': fotos_slider
    }
    return render(request, 'app/home.html', data)  # data as a third param


def contacto(request):
    # if form Contacto is empty(template) it'll be sent right back here
    data = {
        'form': ContactoForm()  # Instantiating a new empty form
    }

    # POST indicates a form with data was submit
    # POST is a dict with data
    if request.method == 'POST':
        # store Contacto form data into this var
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto enviado! :)"

        data["form"]: formulario

    return render(request, 'app/contacto.html', data)


def mision(request):

    fotos_galeria = Galeria.objects.all()
    mision = Mision.objects.all().first()
    vision = Vision.objects.all().first()
    data = {
        'galeria': fotos_galeria,
        'mision': mision,
        'vision': vision
    }
    return render(request, 'app/mision.html', data)
