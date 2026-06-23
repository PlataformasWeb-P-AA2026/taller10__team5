from django.shortcuts import render

from django.shortcuts import render, redirect
from ordenamiento.models import Parroquia, Barrio, PresidenteBarrio
from ordenamiento.forms import ParroquiaForm, BarrioForm

def index(request):
    
    parroquias = Parroquia.objects.all()
    
    informacion_template = {'parroquias': parroquias}
    return render(request, 'index.html', informacion_template)

def listar_parroquias(request):
    parroquias = Parroquia.objects.all()
    return render(request, 'listarParroquias.html', {
        'parroquias': parroquias,
    })


def listar_barrios(request):
    barrios = Barrio.objects.all()
    return render(request, 'listarBarrios.html', {
        'barrios': barrios,
    })


def crear_parroquia(request):
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_parroquias)
    else:
        formulario = ParroquiaForm()
    return render(request, 'crearParroquia.html', {'formulario': formulario})


def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_parroquias)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    return render(request, 'editarParroquia.html', {'formulario': formulario})


def crear_barrio(request):
    if request.method == 'POST':
        formulario = BarrioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_barrios)
    else:
        formulario = BarrioForm()
    return render(request, 'crearBarrio.html', {'formulario': formulario})


def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        if formulario.is_valid():
            formulario.save()
            return redirect(listar_barrios)
    else:
        formulario = BarrioForm(instance=barrio)
    return render(request, 'editarBarrio.html', {'formulario': formulario})