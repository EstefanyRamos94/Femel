from django.contrib import admin
from notificaciones.util.admin import AbstractNotificacionAdmin

# Register your models here.
from .models import Notificaciones

admin.site.register(Notificaciones, AbstractNotificacionAdmin)