from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from fondo.models import LineaCredito, SolicitudCredito
from django.db import connection

# Create your views here.
class HomePageView(ListView):
    # Atributo que indica que template html debe usar:
    template_name = 'core/index.html'
    model = SolicitudCredito

   

class TeamPageView(TemplateView):
    template_name = 'core/team.html'
    team_dict = {
        'autor': 'María Estefany Morales Ramos',
        'universidad': 'Institución Universitaria Politécnico Grancolombiano',
        'facultad': 'Facultad, Departamento (Diseño, Ingeniería e innovación)',
        'ubicacion' : 'Medellín, Colombia',
        'periodo' : '2021',
        'repositorio': 'https://github.com/EstefanyRamos94/Femel'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.team_dict)

class LineasPageView(ListView):
    template_name = 'core/lineas.html'
    model = LineaCredito

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, self.datos)