from django.contrib import admin
from .models import Poliza,Usuario, Auto
# Register your models here.

@admin.register(Poliza)
class PolizaAdmin(admin.ModelAdmin):
        list_display = ("nombre", "precio", "categoria")
        list_filter = ("nombre", "precio", "categoria")
        search_fields = ("nombre", "precio", "categoria")

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
        list_display = ("nombre","edad","registro")
        list_filter = ("nombre","edad","registro")
        search_fields = ("nombre","edad","registro")

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
        list_display=("marca","modelo","color","placa","kilometraje")
        list_filter=("marca","modelo","color","placa","kilometraje")
        search_fields=("marca","modelo","color","placa","kilometraje")
