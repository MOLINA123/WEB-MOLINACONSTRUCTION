


from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms
from django.conf import settings


def contacto(request):
    contact_form = ContactForms()

    if request.method == "POST":
        contact_form = ContactForms(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "MOLINACONSTRUCTION: Nuevo mensaje de contacto",
                "Nombre {}\nEmail: {}\nMensaje:\n{}".format(name, email, content),
                "",
                ["molinaconstruction2021@gmail.com"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contacto')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contacto')+"?fail")
    
    return render(request, "contact/contact.html",{'form':contact_form})
