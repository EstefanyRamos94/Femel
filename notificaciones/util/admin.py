from ast import List
from asyncio import ReadTransport
from os import listdir
from pickletools import read_uint4
from django.contrib import admin

class AbstractNotificacionAdmin(admin.ModelAdmin):
    raw_id_fields = ('destino',)
    List_display = ('destino','actor','verbo', 'read', 'publico')
    list_filter = ('nivel','read')

    def get_queryset(self, request):
        qs = super(AbstractNotificacionAdmin, self).get_queryset(request)
        return qs.prefetch_related('actor')