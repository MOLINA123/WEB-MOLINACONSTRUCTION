from unicodedata import name
from django.contrib import admin
from .models import *

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='personal').exists():
            return ('key', 'name')
        else:
            return ('created','updated')


admin.site.register(Link, LinkAdmin)

# Register your models here.
