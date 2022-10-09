from django.http import HttpResponse
from datetime import datetime
from . import views
from django.template import Context, Template


def hola(request):
    return HttpResponse("Hola hola")


def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year-edad
    return HttpResponse(f'tu fecha de nacimiento aproximada para tus {edad} años es {fecha}')


def mi_index(request):

    cargar_archivo = open(
        r'C:\Users\Juan Carlos Diaz\Desktop\jcintermedio\template\index.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)
