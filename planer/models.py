from django.db import models
from datetime import date, datetime

# Función para extraer el año actual del servidor
def periodoActual():
    hoy = datetime.year
    return hoy

# Create your models here.
class Periodo(models.Model):
    periodo = models.IntegerField(verbose_name="Año de ejecución", default=periodoActual, null=False, max_length=4)
    estado_periodo = models.CharField(verbose_name="Estado de Periodo", max_length=20, default="Activo")
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        pass

    def __str__(self) -> str:
        return self.periodo 

class Meses(models.Model):
    pass
