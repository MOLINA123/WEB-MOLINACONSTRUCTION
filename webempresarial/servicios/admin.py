from django.contrib import admin

from .models import *

#para created y update sea solo lectura

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ColumnaAlquilerAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PlanoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class LosaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class GypsumAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')




admin.site.register(Service, ServiceAdmin)
admin.site.register(ColumnaAlquiler, ColumnaAlquilerAdmin)
admin.site.register(Plano, PlanoAdmin)
admin.site.register(Losa, LosaAdmin)
admin.site.register(Gypsum,GypsumAdmin)


