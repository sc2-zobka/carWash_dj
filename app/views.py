from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio, Slider, Galeria, Vision, Mision, Insumo
from .forms import ContactoForms, InsumoForms, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def home(request):
    servicios = Servicio.objects.all()
    sliders = Slider.objects.all()
    data = {
        "servicios": servicios,
        "sliders": sliders
    }

    return render(request, 'app/index.html', data)

def contacto(request):
    data = {
        "form": ContactoForms()
    }

    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            
            messages.success(request, "Contacto enviado!")
        data["form"] = formulario

    return render(request, 'app/contacto.html', data)

@login_required
@permission_required('app.add_insumo')
def insumos(request):
    insumos = Insumo.objects.get_queryset().order_by('id')
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(insumos, 3)
        insumos = paginator.page(page)
    except:
        raise Http404
    

    data = {
        "form": InsumoForms(),
        "entity": insumos,
        "paginator": paginator,
    }

    if request.method == 'POST':
        formulario = InsumoForms(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()

            messages.success(request, "Insumo creado!")
        data["form"] = formulario

    return render(request, 'app/insumos.html', data)

@login_required
@permission_required('app.change_insumo')
def modificar_insumo(request, id):
    #insumo = Insumo.objects.get(id=id)
    insumo = get_object_or_404(Insumo, id=id)
    data = {
        "form": InsumoForms(instance=insumo)
    }

    if request.method == 'POST':
        formulario = InsumoForms(data=request.POST, instance=insumo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "El registro ha sido modificado!")
            return redirect(to="insumos")
        data["form"] = formulario

    return render(request, 'app/modificar_insumo.html', data)

@login_required
@permission_required('app.delet_insumo')
def eliminar(request, id):
    #insumo = Insumo.objects.get(id=id)
    insumo = get_object_or_404(Insumo, id=id)
    insumo.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="insumos")

def mision(request):
    galerias = Galeria.objects.all()
    vision = Vision.objects.all().first()
    mision = Mision.objects.all().first()
    data = {
        "galerias": galerias,
        "vision": vision,
        "mision": mision
    }
    return render(request, 'app/mision.html', data)

def registro(request):
    data = {
        "form": CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                    username=formulario.cleaned_data["username"],
                    password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)