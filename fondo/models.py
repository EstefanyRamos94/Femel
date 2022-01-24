from django.db.models import CASCADE
from django.db import models
from django.contrib.auth.models import User
from core.types.sino import SiNo
from core.types.vinculacion import Vinculacion
from core.types.plazos import PlazoMaximo
from core.types.estadosolicitud import EstadoSolicitud
from ckeditor.fields import RichTextField

# Funciones adicionales:

def subir_documentos(instance, filename): 
    return 'recursos/docsolicitudes/' + filename

# Create your models here.

class DocumentosRequeridos(models.Model):
    nombre_documento = models.CharField(verbose_name='Nombre de Documento', max_length=255, null=False, unique=True)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Documentos Requeridos'

    def __str__(self):
        return f'{self.nombre_documento}'


class LineaCredito(models.Model):
    nombre_linea = models.CharField(verbose_name='Linea de Crédito', max_length=120, null=False)
    destino = RichTextField(verbose_name="Uso de Linea de Crédito", null=True, blank=True)
    documento_requerido = models.ManyToManyField(DocumentosRequeridos, verbose_name="Documentos Requeridos")
    consulta_riesgo = models.CharField(verbose_name='Consulta en Central de Riesgo', max_length=2, choices=SiNo)
    periodo_vinculacion = models.CharField(verbose_name='Periodo Minimo de Vinculación', max_length=10, choices=Vinculacion)
    plazo_maximo = models.CharField(verbose_name='Plazo Máximo', max_length=10, choices=PlazoMaximo)
    legalizacion = RichTextField(verbose_name="Legalización", null=True, blank=True)
    soportes = RichTextField(verbose_name="Soportes para Legalización", null=True, blank=True)
    inhabilidades = RichTextField(verbose_name="Inhabilidades", null=True, blank=True)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Linea de Crédito'

    def __str__(self) -> str:
        return f'{self.nombre_linea}'

class SolicitudCredito(models.Model):
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    credito = models.ForeignKey(LineaCredito, on_delete=CASCADE)
    monto_credito = models.DecimalField(verbose_name='Monto a Solicitar', decimal_places=2, max_digits=10)
    plazo_credito = models.PositiveIntegerField(verbose_name="Plazo en meses")
    estado_solicitud = models.CharField(verbose_name='Estado de Solicitud', max_length=20, null=False, choices=EstadoSolicitud, default='Sin Atender')
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Solicitudes de Crédito'

    def __str__(self):
        return f'{self.usuario}'

class DetalleSolicitudes(models.Model):
    solicitud = models.ForeignKey(SolicitudCredito, on_delete=CASCADE)
    nota_solicitud = RichTextField(verbose_name="Notas de solicitud - Seguimientos", null=True, blank=True)
    valor_aprobado = models.DecimalField(verbose_name="Monto Aprobado", max_digits=10, decimal_places=2, null=False)
    fecha_desembolso = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha de Desembolso", null=True, blank=True)
    soportes_solicitud = models.FileField(verbose_name="Soportes", upload_to=subir_documentos, null=True, blank=True)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Gestión de Solicitudes'

    def __str__(self) -> str:
        return f'{self.solicitud}'

