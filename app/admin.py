from django.contrib import admin
from .models import Insumo, Servicio, Contacto, Slider, Galeria, Mision, Vision

class InsumoAdmin(admin.ModelAdmin):
    list_display = "nombre", "precio", "stock", "imagen"
    search_fields = ["nombre"]
    sortable_by = ["precio", "stock"]
    list_per_page = 10

class ServicioAdmin(admin.ModelAdmin):
    list_display = "nombre", "precio", "descripcion", "imagen"
    search_fields = ["nombre"]
    sortable_by = ["precio"]
    list_per_page = 10

class ContactoAdmin(admin.ModelAdmin):
    list_display = "nombre", "telefono", "email", "mensaje"
    search_fields = ["nombre", "email"]
    list_per_page = 10

class SliderAdmin(admin.ModelAdmin):
    list_display = "nombre", "imagen"
    search_fields = ["nombre"]
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display = "nombre", "imagen"
    search_fields = ["nombre"]
    list_per_page = 10

class MisionAdmin(admin.ModelAdmin):
    list_display = "nombre", "mensaje",
    search_fields = ["nombre"]
    list_per_page = 10

class VisionAdmin(admin.ModelAdmin):
    list_display = "nombre", "mensaje",
    search_fields = ["nombre"]
    list_per_page = 10

# Register your models here.
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Mision, MisionAdmin)
admin.site.register(Vision, VisionAdmin)

admin.site.site_header = "Administración de CarWash"
admin.site.site_title = "CarWash"
admin.site.index_title = "Sitio Admnistrativo de CarWash"