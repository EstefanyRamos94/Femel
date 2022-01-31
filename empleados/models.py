from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from core.types.estadoempleado import EstadoEmpleado
from core.types.tipocontrato import Contratos
from core.types.licenciasconduccion import Licencias
from core.types.sino import SiNo
from core.types.tipovivienda import Vivienda
from core.types.estadoempleado import EstadoEmpleado

# Create your models here.
class Empleados(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE)
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso", auto_now=False, auto_now_add=False)
    contrato = models.CharField(verbose_name='Tipo de Contrato', max_length=100, choices=Contratos)
    correo_institucional = models.EmailField(verbose_name='Correo Institucional', unique=True, blank=True, null=True)
    cargo= models.CharField(verbose_name='Cargo Ocupado', max_length=180)
    estado = models.CharField(verbose_name='Condición Actual del Empleado', max_length=40, choices=EstadoEmpleado, default='Empleado/Activo')
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Empleados'
        ordering = ['usuario__username']

    def __str__(self):
        return f'{self.usuario}'

class DatosEmpleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE, verbose_name='Empleado')
    tipo_sangre = models.CharField(verbose_name='Tipo de Sangre', max_length=3)
    persona_contacto = models.CharField(verbose_name='Persona de contacto', max_length=25)
    telefonos_contacto = models.CharField(verbose_name='Telefono de contacto', max_length=25)
    licencia_conduccion = models.CharField(verbose_name='Licencia de conducción', max_length=25, choices=Licencias, default='Ninguna')
    vehiculo = models.CharField(verbose_name='Posee Vehiculo', max_length=2, choices=SiNo, default='No')
    tipo_vivienda = models.CharField(verbose_name='Tipo de vivienda', max_length=20, choices=Vivienda)
    direccion_casa = models.TextField(verbose_name='Dirección Residencia', null=True, blank=True)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Datos de Empleados'
        ordering = ['usuario__username']

    def __str__(self):
        return f'{self.usuario}'
    