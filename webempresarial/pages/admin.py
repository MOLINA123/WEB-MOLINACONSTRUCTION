from django.contrib import admin
from .models import *

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ('title', 'order')


admin.site.register(Page, PageAdmin)

# Register your models here.

# Register your models here.
