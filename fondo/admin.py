from django.contrib import admin
from .models import *

# Register your models here.
class LineaCreditoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('nombre_linea','consulta_riesgo','periodo_vinculacion','plazo_maximo')
    ordering = ('nombre_linea','consulta_riesgo')
    search_fields = ('nombre_linea','consulta_riesgo','periodo_vinculacion','plazo_maximo')

    class Meta:
        model = LineaCredito

class DocumentosRequeridosAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('nombre_documento',)
    ordering = ('nombre_documento',)
    search_fields = ('nombre_documento',)

    class Meta:
        model = DocumentosRequeridos

class SolicitudesCreditoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('usuario','credito', 'monto_credito')
    ordering = ('usuario',)
    search_fields = ('usuario','credito', 'monto_credito')

    class Meta:
        model = SolicitudCredito

class DetalleSolicitudesAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('solicitud',)
    ordering = ('solicitud',)
    search_fields = ('solicitud',)

    class Meta:
        model = DetalleSolicitudes


admin.site.register(LineaCredito, LineaCreditoAdmin)
admin.site.register(DocumentosRequeridos, DocumentosRequeridosAdmin)
admin.site.register(SolicitudCredito, SolicitudesCreditoAdmin)
admin.site.register(DetalleSolicitudes, DetalleSolicitudesAdmin)