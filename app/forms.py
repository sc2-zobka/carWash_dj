from django import forms
from .models import Contacto, Insumo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        
        raise forms.ValidationError('This email address is already in use.')

    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username",  "email", "password1", "password2"]