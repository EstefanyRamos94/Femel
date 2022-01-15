from django.db import models
from core.types.sino import SiNo
from core.types.vinculacion import Vinculacion
from core.types.plazos import PlazoMaximo
from ckeditor.fields import RichTextField

# Create your models here.

class LineaCredito(models.Model):
    nombre_linea = models.CharField(verbose_name='Linea de Crédito', max_length=120, null=False)
    destino = RichTextField(verbose_name="Uso de Linea de Crédito", null=True, blank=True)
    consulta_riesgo = models.CharField(verbose_name='Consulta en Central de Riesgo', max_length=2, choices=SiNo)
    periodo_vinculacion = models.CharField(verbose_name='Periodo Minimo de Vinculación', max_length=10, choices=Vinculacion)
    plazo_maximo = models.CharField(verbose_name='Plazo Máximo', max_length=10, choices=PlazoMaximo)

    class Meta:
        verbose_name_plural = 'Linea de Crédito'

    def __str__(self) -> str:
        return f'{self.nombre_linea}'