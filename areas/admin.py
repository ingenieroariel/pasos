from areas.models import *
from django.contrib.gis import admin

class ResguardoAdmin(admin.GeoModelAdmin):
    list_display = ['nombre', 'familias', 'poblacion', 'resolucion', 'etnia']
    list_filter = ['etnia',]
    search_fields = ['nombre', 'etnia', 'resolucion']

admin.site.register(AreaProtegida, admin.GeoModelAdmin)
admin.site.register(Resguardo,ResguardoAdmin)
