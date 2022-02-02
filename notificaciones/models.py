from notificaciones.util.models import AbstractNotificacion
from django.db import models

# Clase abstracta de notificaciones:
class Notificaciones(AbstractNotificacion):
    
    class Meta(AbstractNotificacion.Meta):
        abstract = False