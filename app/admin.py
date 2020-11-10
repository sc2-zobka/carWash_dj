from django.contrib import admin
from .models import Servicio, Slider, Galeria, Mision, \
    Vision, Contacto  # Insumo


class ServicioAdmin(admin.ModelAdmin):
    """
        Display components on "Servicio" admin section
        based on Servicio model's fields
    """
    # display column’s title on list_view
    list_display = ["nombre", "precio", "descripcion"]
    # display a search box tool
    search_fields = ["nombre"]
    # display a filter tool
    list_filter = ["nombre"]
    # display paginator at the bottom of the list_view
    list_per_page = 1


class SilderAdmin(admin.ModelAdmin):
    """
        Display components on "Slider" admin section
        based on Slider model's fields
    """
    list_display = ["nombre", "descripcion", "imagen"]
    search_fields = ["nombre", "imagen"]
    list_filter = ["nombre", "imagen"]
    list_per_page = 3


class GaleriaAdmin(admin.ModelAdmin):
    """
        Display components on "Galeria" admin section
        based on Galeria model's fields
    """
    list_display = ["nombre", "descripcion", "imagen"]
    search_fields = ["nombre", "imagen"]
    list_filter = ["nombre", "imagen"]
    list_per_page = 6


class MisionAdmin(admin.ModelAdmin):
    """
        Display components on "Mision" admin section
        based on Mision model's fields
    """

    def has_add_permission(self, request):
        # allow only one instance of a Mision object

        MAX_OBJECTS = 1
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

    def descripcion_corta(self):
        # display only first 50 characters of 'descripcion' field
        # on Vision admin tree view

        return ("%s..." % (self.descripcion[:50]))

    # avoid displaying full column’s title and set an alias
    descripcion_corta.short_description = 'Descripción'
    list_display = ["nombre", descripcion_corta]
    search_fields = ["nombre"]
    list_filter = ["nombre"]
    list_per_page = 2


class VisionAdmin(admin.ModelAdmin):
    """
        Display components on "Vision" admin section
        based on Vision model's fields
    """

    def has_add_permission(self, request):
        # allow only one instance of a Vision object
        MAX_OBJECTS = 1
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)

    def descripcion_corta(self):
        # display only first 50 characters of 'descripcion' field
        # on Vision admin tree view

        return ("%s..." % (self.descripcion[:50]))

    # avoid displaying full column’s title and set an alias
    descripcion_corta.short_description = 'descripción'
    list_display = ["nombre", descripcion_corta]
    search_fields = ["nombre"]
    list_filter = ["nombre"]
    list_per_page = 2


class ContactoAdmin(admin.ModelAdmin):
    """
        Display components on "Contacto" admin section
        based on Contacto model's fields
    """
    list_display = ["nombre"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]
    list_per_page = 2


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Slider, SilderAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Mision, MisionAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(Contacto, ContactoAdmin)

# change admin title
admin.site.site_header = "Administración Car Wash"
# change admin site title
admin.site.site_title = "CarWash"
# change admin index title
admin.site.index_title = "Administración"
