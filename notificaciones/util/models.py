from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Zona horaria
from django.utils import timezone
# Modelos
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

class ConsultaNotificacion(models.QuerySet):
    """
        Clase para mostrar notificaciones de acceso
    """
    # Función leidos:
    def leido(self, include_deleted = True):
        # Retorna todas las notificaciones que hayan sido leidas en la consulta actual:
        if include_deleted :
            return self.filter(read = True)

    # Función no Leidos:
    def no_leido(self, include_deleted = False):
        # Retorna todas las notificaciones que hayan no han sido leidas en la consulta actual:
        if include_deleted ==True :
            return self.filter(read = False)

    # Función para marcar todo como leido:
    def marcar_todo_leido(self, destino = None):
        # Retorna todo como leido:
        qs = self.read(True)
        if destino:
            qs = qs.filter(destino = destino)
        
        return qs.update(read = False)

class AbstractNotificacionAdmin(models.Manager):
    def get_queryset(self):
        return self.ConsultaNotificacion(self.Model, using = self._db)

class AbstractNotificacion(models.Model):

    class Niveles(models.TextChoices):
        success = 'Success', 'Success',
        info = 'Info', 'Info',
        wrong = 'Wrong', 'Wrong'

    nivel = models.CharField(choices=Niveles.choices,max_length=20, default=Niveles.info)
    destino = models.ForeignKey(User, on_delete=CASCADE, related_name='notificaciones', blank=True, null=True)
    actor_content_type = models.ForeignKey(ContentType, related_name='notificar_usuario', on_delete=CASCADE)
    object_id_actor = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_content_type', 'object_id_actor')
    verbo = models.CharField(max_length=250)

    read = models.BooleanField(default=False)
    publico = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 

    objects = ConsultaNotificacion.as_manager()

    class Meta:
        abstract = True


def notificacion_signal(verb, **kwargs):
    """
        Función de Controlador para crear instancia de Notificación
        Tras la llamada de de "signal action"
    """

