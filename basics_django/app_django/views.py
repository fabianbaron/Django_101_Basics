from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def pagina_home(request):
    return HttpResponse('<h1>Página de Home de la Web App app_django</h1>')

def pagina_contenido(request):
    return HttpResponse('<h1>Página de contenido</h1>')

def pagina_contacto(request):
    return HttpResponse('<h1>Página de contacto</h1>')