from django.contrib import admin
from .models import Servicio, Slider  # Insumo

# Register your models here.


class ServicioAdmin(admin.ModelAdmin):
    '''
        Display components on "Servicio" admin section
        based on Servicio model's fields
    '''
    # display column's header on list_view
    list_display = ["nombre", "precio", "descripcion"]
    # display a search tool
    search_fields = ["nombre"]
    # display a filter tool
    list_filter = ["nombre"]
    # display paginator at the bottom of the list_view
    list_per_page = 1


class SilderAdmin(admin.ModelAdmin):
    '''
        Display components on "Slider" admin section
        based on Silder model's fields
    '''
    list_display = ["nombre", "descripcion", "imagen"]
    search_fields = ["nombre", "imagen"]
    list_filter = ["nombre", "imagen"]
    list_per_page = 1


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Slider, SilderAdmin)

# change admin title
admin.site.site_header = "Administración Car Wash"
# change admin site title
admin.site.site_title = "CarWash"
# change admin index title
admin.site.index_title = "Administración"
