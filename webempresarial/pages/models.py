
from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):

    
    title = models.CharField(verbose_name='titulo', max_length=100, )
    content = RichTextField(verbose_name='contenido')
    order = models.SmallIntegerField(verbose_name='orden de las paginas', default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizació')

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = [ 'order', 'title']

    def __str__(self):
        return self.title


