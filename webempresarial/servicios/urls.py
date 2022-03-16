from django.urls import path
from .  import views


app_name = 'servicios'

urlpatterns = [
    
    path('', views.servicios, name = 'servicios'),
    path('colu/', views.colu, name = 'coluna'),
    path('plano/', views.plano, name = 'plano'),
    path('losa/', views.losa, name = 'losa'),
    path('gypsum/', views.gypsum, name = 'gypsum')
]


   