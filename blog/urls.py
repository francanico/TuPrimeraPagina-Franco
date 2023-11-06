from . import views
from django.urls import path

urlpatterns = [
    path("IturbeSeguros/", views.index, name= "IturbeSeguros"),
    path("polizas/", views.poliza, name= "poliza"),
    path("polizas/crearpoliza/",views.form_poliza, name="crear_poliza"),
    path("usuario/crearusuario/",views.form_usuario, name="crear_usuario"),
    path("usuario/",views.usuario, name="usuario"),
    path("buscador/",views.buscador, name="buscador"),
    path("buscadoruser/",views.buscador_usuario, name="buscadoruser"),
    path("auto/",views.auto, name="auto"),
    path("auto/crearauto/",views.form_auto, name="crear_auto"),
    path("buscadorauto/",views.buscar_auto, name="buscarauto"),
]