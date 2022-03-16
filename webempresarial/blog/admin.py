from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['title', 'author', 'published']
    ordering = ['author', 'published']
    search_fields = ['title', 'content']
    date_hierarchy = 'published'
    list_filter = ['author__username', 'categories__name']

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])

    post_categories.short_descriptions = 'categorias'


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

# Register your models here.
