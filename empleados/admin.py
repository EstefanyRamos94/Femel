from pyexpat import model
from django.contrib import admin
from .models import *

# Register your models here.
class EmpleadosAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at','estado')  # no permite modificar estos campos
    list_display = ('usuario', 'cargo', 'contrato','estado')
    ordering = ('cargo','contrato')
    search_fields = ('cargo',)

    class Meta:
        model = Empleados

class DatosEmpleadosAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('usuario','persona_contacto','telefonos_contacto','tipo_vivienda','tipo_sangre')
    ordering = ('usuario',)
    search_fields = ('usuario','persona_contacto','telefonos_contacto','tipo_vivienda','tipo_sangre')

    class Meta:
        model = DatosEmpleado

admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(DatosEmpleado, DatosEmpleadosAdmin)

