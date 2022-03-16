from django.db import models
class Link(models.Model):

    key = models.SlugField(verbose_name='nombre de clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='nombre', max_length=100, )
    url = models.URLField(verbose_name='link', null=True, blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizació')

    class Meta:
        verbose_name = 'red social'
        verbose_name_plural = 'redes sociales'
        ordering = ['-created']

    def __str__(self):
        return self.name


# Create your models here.
