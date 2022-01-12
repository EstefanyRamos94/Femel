from django.urls import path 
from django.urls.resolvers import URLPattern

from .views import ProfileUpdate, PqrsCreate

urlpatterns = [ 
    path("profile/", ProfileUpdate.as_view(),name= "profile"),
    path("pqrs/", PqrsCreate.as_view(),name= "pqrs"),
    #path("respuesta/", ProfileUpdate.as_view(),name= "respuesta"),
 ]