from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

#_____________Plantas_____________#
def plantas(request):
    contexto = {'plantas': Planta.objects.all()}
    return render(request, "aplicacion/plantas.html", contexto)

def plantasForm(request):
    if request.method == "POST":
        miForm = PlantaForm(request.POST)
        if miForm.is_valid():
            planta_nombre = miForm.cleaned_data.get("nombre")
            planta_ambiente = miForm.cleaned_data.get("ambiente")
            planta_riego = miForm.cleaned_data.get("riego")
            planta_iluminacion = miForm.cleaned_data.get("iluminacion")
            planta_tamaño = miForm.cleaned_data.get("tamaño")
            planta = Planta(nombre=planta_nombre, ambiente=planta_ambiente, riego=planta_riego, iluminacion= planta_iluminacion, tamaño=planta_tamaño)
            planta.save()
            return redirect(reverse_lazy('plantas'))
            # return render(request,"aplicacion/home.html")
    else:
        miForm = PlantaForm()
    return render(request, "aplicacion/plantasForm.html",{"form":miForm})

def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarPlantas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        plantas = Planta.objects.filter(nombre__icontains=patron)
        contexto= {"plantas":plantas}
        return render(request, "aplicacion/plantas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")


#_____________Macetas_____________#
def macetas(request):
    contexto = {'macetas': Maceta.objects.all()}
    return render(request, "aplicacion/macetas.html", contexto)

def macetasForm(request):
    if request.method == "POST":
        miForm = MacetaForm(request.POST)
        if miForm.is_valid():
            maceta_material = miForm.cleaned_data.get("material")
            maceta_forma = miForm.cleaned_data.get("forma")
            maceta_tamaño = miForm.cleaned_data.get("tamaño")
            macetas_color = miForm.cleaned_data.get("color")
            maceta = Maceta(material=maceta_material, forma=maceta_forma, tamaño=maceta_tamaño, color= macetas_color)
            maceta.save()
            return redirect(reverse_lazy('macetas')) 
            #return render(request,"aplicacion/home.html")
    else:
        miForm = MacetaForm()
    return render(request, "aplicacion/macetasForm.html",{"form":miForm})


#_____________Fertilizantes_____________#
def fertilizantes(request):
    contexto = {'fertilizantes': Fertilizante.objects.all()}
    return render(request, "aplicacion/fertilizantes.html",contexto)


def fertilizantesForm(request):
    if request.method == "POST":
        miForm = FertilizanteForm(request.POST)
        if miForm.is_valid():
            fertilizante_nombre = miForm.cleaned_data.get("nombre")
            fertilizante_nutrientes = miForm.cleaned_data.get("nutrientes")
            fertilizante_dosis = miForm.cleaned_data.get("dosis")
            fertilizante_precauciones = miForm.cleaned_data.get("precauciones")
            fertilizante = Fertilizante(nombre=fertilizante_nombre, nutrientes=fertilizante_nutrientes, dosis=fertilizante_dosis, precauciones= fertilizante_precauciones)
            fertilizante.save()
            return redirect(reverse_lazy('fertilizantes')) 
            #return render(request,"aplicacion/home.html")
    else:
        miForm = FertilizanteForm()
    return render(request, "aplicacion/fertilizantesForm.html",{"form":miForm})
