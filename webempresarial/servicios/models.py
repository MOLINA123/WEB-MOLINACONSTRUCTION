
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'titulo')
    subtitle = models.CharField(max_length=200, verbose_name='sustitulo')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='imagen', upload_to= 'servicios')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizació')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title


class ColumnaAlquiler(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'titulo')
    pre = models.CharField(max_length=10, verbose_name= 'precio')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='imagen', upload_to= 'servicios')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizació')

    class Meta:
        verbose_name = 'columna'
        verbose_name_plural = 'columnas'
        ordering = ['-created']

    def __str__(self):
        return self.title



class Plano(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'titulo')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='imagen', upload_to= 'servicios')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizació')

    class Meta:
        verbose_name = 'plano'
        verbose_name_plural = 'planos'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Losa(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'titulo')
    pre = models.CharField(max_length=10, verbose_name= 'precio')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='imagen', upload_to= 'servicios')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizació')
    
    class Meta:
        verbose_name = 'losa'
        verbose_name_plural = 'losas'
        ordering = ['-created']
        

    def __str__(self):
        return self.title

class Gypsum(models.Model):
    title = models.CharField(max_length=200, verbose_name= 'titulo')
    pre = models.CharField(max_length=10, verbose_name= 'precio')
    content = models.TextField(verbose_name='contenido')
    image = models.ImageField(verbose_name='imagen', upload_to= 'servicios')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizació')

    class Meta:
        verbose_name = 'gypsum'
        verbose_name_plural = 'gypsums'
        ordering = ['-created']

    def __str__(self):
        return self.title
