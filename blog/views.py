from django.shortcuts import render, redirect
from .models import Poliza,Usuario, Auto
from .forms import PolizaForm,UsuarioForm,AutoForm

# Create your views here.
def index(request):
    return render(request, "IturbeSeguros.html")

def poliza(request):
    polizas = Poliza.objects.all()
    return render(request,"poliza.html",{"polizas": polizas})

def form_poliza(request):
    if request.method == "POST":
        form1 = PolizaForm(request.POST)
        if form1.is_valid():
            poliza = form1.save()
            return redirect("poliza")
    else:
        form1= PolizaForm
    return render (request,"crear_poliza.html",{"form1": form1})

def form_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect("usuario")
    else:
        form= UsuarioForm
    return render (request,"crear_usuario.html",{"form": form})

def usuario(request):
    usuarios= Usuario.objects.all()
    return render(request,"usuario.html",{"usuarios": usuarios})

def buscador(request):

    categoria = request.GET.get("categoria")

    if categoria:

        polizas=Poliza.objects.filter(categoria__icontains= categoria)
        return render(request,"buscador.html",{"polizas": polizas, "categoria": categoria})
    
    else:
        respuesta= "No enviaste Datos"

    return render(request,"buscador.html",{"respuesta": respuesta})

def buscador_usuario(request):

    nombre = request.GET.get("usuario")

    if nombre:

        names=Usuario.objects.filter(nombre__icontains= nombre)
        return render(request,"buscador_user.html",{"names": names, "nombre": nombre})
    
    else:
        respuesta= "No enviaste Datos"

    return render(request,"buscador_user.html",{"respuesta": respuesta})

def auto(request):
    auto = Auto.objects.all()
    return render(request,"auto.html",{"auto": auto})

def form_auto(request):

    if request.method == "POST":
        formuauto= AutoForm(request.POST)
        if formuauto.is_valid():
            auto= formuauto.save()
            return redirect("auto")
    else:
        formuauto= AutoForm
    return render (request,"crear_auto.html",{"formuauto": formuauto})

def buscar_auto(request):

    placa = request.GET.get("placa")

    if placa:

        placas=Auto.objects.filter(placa__icontains= placa)
        return render(request,"buscar_auto.html",{"placas":placas,"placa": placa})
    
    else:
        respuesta= "No enviaste Datos"

    return render(request,"buscar_auto.html",{"respuesta": respuesta})