from django.urls import path
from .views import SolicitudesDetailView, SolicitudesCreate,SolicitudesUpdate

fondo_patterns = ([
    path('', SolicitudesCreate.as_view(), name='solicitudes'),
    path('<int:pk>/<slug:slug>/', SolicitudesDetailView.as_view(), name='solicitudes-usuario'),
    path('nueva-solicitud/', SolicitudesCreate.as_view(), name='nuevasolicitud'),
    path('update/<int:pk>/', SolicitudesUpdate.as_view(), name='update'),
], 'fondo')