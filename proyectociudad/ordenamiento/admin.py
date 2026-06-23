from django.contrib import admin
from ordenamiento.models import Parroquia,Barrio,PresidenteBarrio

class ParroquiaAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre', 'ubicacion')

admin.site.register(Parroquia, ParroquiaAdmin)


class BarrioaAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'numero_viviendas', 'numero_parques','numero_edificios_residenciales','parroquia')
    search_fields = ('nombre', 'parroquia')

admin.site.register(Barrio, BarrioaAdmin)

class PresidenteBarrioAdmin(admin.ModelAdmin):
    
    list_display = ('cedula', 'nickname', 'edad','profesion','barrio')
    search_fields = ('nombre', 'nickname')
 
admin.site.register(PresidenteBarrio,PresidenteBarrioAdmin)