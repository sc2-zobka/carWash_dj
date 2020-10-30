from django.contrib import admin
from .models import Servicio, Slider, Galeria, Mision  # Insumo


class ServicioAdmin(admin.ModelAdmin):
    '''
        Display components on "Servicio" admin section
        based on Servicio model's fields
    '''
    # display column's header on list_view
    list_display = ["nombre", "precio", "descripcion"]
    # display a search box tool
    search_fields = ["nombre"]
    # display a filter tool
    list_filter = ["nombre"]
    # display paginator at the bottom of the list_view
    list_per_page = 1


class SilderAdmin(admin.ModelAdmin):
    '''
        Display components on "Slider" admin section
        based on Slider model's fields
    '''
    list_display = ["nombre", "descripcion", "imagen"]
    search_fields = ["nombre", "imagen"]
    list_filter = ["nombre", "imagen"]
    list_per_page = 1


class GaleriaAdmin(admin.ModelAdmin):
    '''
        Display components on "Galeria" admin section
        based on Galeria model's fields
    '''
    list_display = ["nombre", "descripcion", "imagen"]
    search_fields = ["nombre", "imagen"]
    list_filter = ["nombre", "imagen"]
    list_per_page = 1


class MisionAdmin(admin.ModelAdmin):
    '''
        Display components on "Mision" admin section
        based on Mision model's fields
    '''
    list_display = ["nombre", "descripcion"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]
    list_per_page = 2


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Slider, SilderAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Mision, MisionAdmin)

# change admin title
admin.site.site_header = "Administración Car Wash"
# change admin site title
admin.site.site_title = "CarWash"
# change admin index title
admin.site.index_title = "Administración"
