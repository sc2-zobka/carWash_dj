from django import forms
from .models import Contacto, Insumo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class ContactoForms(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "telefono", "email", "mensaje"]

class InsumoForms(forms.ModelForm):
    nombre = forms.CharField(required=True, min_length=3, max_length=120)
    precio = forms.IntegerField(required=True, min_value=1)
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(required=False, min_length=3, max_length=200)
    stock = forms.IntegerField(required=True, min_value=0)

    class Meta:
        model = Insumo
        fields = ["nombre", "precio", "imagen", "descripcion", "stock"]

class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(required=True,  # falta validar solo letras
                             min_length=3,
                             max_length=80,
                             widget=forms.TextInput(attrs=
                                        {'class':'form-control',
                                        'pattern':'[A-Za-z ]+',
                                        'title':'Debe contener solo letras!'}))

    apellido = forms.CharField(required=True,  # falta validar solo letras
                             min_length=3,
                             max_length=80,
                             widget=forms.TextInput(attrs=
                                        {'class':'form-control',
                                        'pattern':'[A-Za-z ]+',
                                        'title':'Debe contener solo letras!'}))
    
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        mensaje = str()

        try:
            User.objects.get(email=email)
            mensaje = "Correo ya se encuentra en uso."

            validate_email(email)
        except User.DoesNotExist:
            return email
        except ValidationError:
            return email

        raise forms.ValidationError(mensaje)

    
    class Meta:
        model = User
        #fields = ["nombre", "apellido", "username",  "email", "password1", "password2"]
        fields = ["nombre", "apellido",
                  "email", "username",
                  "password1", "password2"]