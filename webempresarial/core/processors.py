from .models import BarraMenu

def navegacion(request):
    context = {}
    barramenus = BarraMenu.objects.all()
    for barramenu in barramenus:
        context[barramenu.key] = barramenu.name
    
    return context