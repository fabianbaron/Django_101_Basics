from django.urls import path
from .views import pagina_home, pagina_contacto, pagina_contenido

urlpatterns = [
    path('', pagina_home, name='home'),
    path('contacto/', pagina_contacto, name='contacto'),
    path('contenido/', pagina_contenido, name='contacto'),
]
