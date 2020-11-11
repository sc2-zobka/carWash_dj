from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):
    """
        Form Contacto
    """

    """nombre = forms.CharField(required=True,
                             min_length=3,
                             max_length=80,
                             widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'pattern': '[A-Za-z ]+',
                                        'title': 'Debe contener solo letras!'
                                    }
                                )
                             )
    """
    class Meta:

        model = Contacto
        fields = '__all__'
