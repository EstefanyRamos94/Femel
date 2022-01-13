from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# Vistas basadas en clases:
class HomePageView(TemplateView):
    # Atributo que indica que template html debe usar:
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'titulo': 'FEMEL',
            'mensaje': 'Prototipo funcional para la administración de fondos de empleados',
            'boton': 'Ingresar'

        })
