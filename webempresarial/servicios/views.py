from django.shortcuts import render
from .models import *




def servicios(request):
    project = Service.objects.all()
    context = {
        'project':project
    }
    return render(request, 'servicios/services.html', context)



def colu(request):
    projet = ColumnaAlquiler.objects.all()
    context = {

        'projs':projet
    }
    return render(request, 'servicios/alquiler-cola.html', context)

def plano(request):
    planoA = Plano.objects.all()
    context = {
        'planos':planoA
    }
    return render(request, 'servicios/plano.html', context)

def losa(request):
    losa1 = Losa.objects.all()
    context = {
        'losas':losa1

    }
    return render(request, 'servicios/losa.html', context)


def gypsum(request):
    gyp = Gypsum.objects.all()
    context = {
        'gypsums': gyp

    }
    return render(request, 'servicios/gypsum.html', context)
