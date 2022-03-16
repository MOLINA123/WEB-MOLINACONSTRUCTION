

from django.db import models
from django.utils.timezone import timezone

class HomeModelo(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=100)
    subtitle = models.CharField(verbose_name='Subtitilo', max_length=100)
    image = models.ImageField(verbose_name='Imagen', upload_to='inicio', null =True, blank=True)
    content = models.TextField()

    class Meta:
        verbose_name = 'homemodelo'
        verbose_name_plural = 'homemodelos'

    def __str__(self):
        return self.title



class BarraMenu(models.Model):
    key = models.SlugField(verbose_name='nombre de clave', max_length=100, unique=True)
    referencia = models.CharField(max_length=50)
    name = models.CharField(verbose_name='nombre', max_length=50, null=True, blank= True)

    class Meta:
        verbose_name = 'bara menu'
        verbose_name_plural = 'barra de menus'

    def __str__(self):
        return self.referencia


class Visita(models.Model):
    mensaje_llamado = models.CharField(verbose_name='mensaje de llamado', max_length=100)
    submensaje_llamado = models.CharField(verbose_name='segundo mensaje de llama', max_length=100)
    dias_laborable = models.CharField(verbose_name='dias de oficinas', max_length=50)
    horario = models.CharField(verbose_name='horario', max_length=10)

    horario_sabado = models.CharField(verbose_name='horario del sábado', max_length=100)
    horario_domingo = models.CharField(verbose_name='horario domingo', max_length=100)
    direccion = models.CharField(verbose_name='calle princilap', max_length=100)
    pais_ciudad = models.CharField(verbose_name='ciudad pais', max_length=100)
    llamada_accion = models.CharField(verbose_name='llamada a la acción', max_length=100)
    telefofo = models.CharField(verbose_name='numero de telefono', max_length=9)
    celular = models.CharField(verbose_name='numero celular', max_length=10)
   

    class Meta:
        verbose_name = 'visita'
        verbose_name_plural = 'visitas'

        def __str__(self):
            return self.mensaje_llamado


class Historia(models.Model):
    title = models.CharField(verbose_name='titulo', max_length=100)
    subtitle = models.CharField(verbose_name='subtitulo', max_length=100)
    contenido = models.TextField(verbose_name='historia')
    image = models.ImageField(verbose_name='imagen')

    class Meta:
        verbose_name = 'historia'
        verbose_name_plural = 'historias'

        def __str__(self):
            return self.title
        


    
