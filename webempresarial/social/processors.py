import re



from .models import Link

def contexto(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    
    return context