from django.shortcuts import render
from .models import HomeModelo, Visita, Historia

def home(request):
    projectos = HomeModelo.objects.all()
    context = {
        'projectos': projectos
    }
    return render(request, 'core/home.html', context)


def historia(request):
    histo = Historia.objects.all()
    context = {
        'histos': histo
    }
    return render(request, 'core/about.html', context)



def visitano(request):
    visitas = Visita.objects.all()
    context = {
        'visita': visitas
    }
    return render(request, 'core/store.html', context)





def contacto(request):
    return render(request, 'core/contact.html')

# Create your views here.
