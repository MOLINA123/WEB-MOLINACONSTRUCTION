from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updated = models.DateTimeField(auto_now= True, verbose_name='fecha de actualizacion')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='fecha de publicacioon', default= now)
    image = models.ImageField(verbose_name='imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categoria,verbose_name='categorias', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de publicacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de edición')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title


# Create your models here.
