from django.urls import path
from .  import views


app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('historia/', views.historia, name = 'historia'),
    path('visitanos/', views.visitano, name = 'visitanos'),
   
   
    path('contacto/', views.contacto, name = 'contacto')
]
