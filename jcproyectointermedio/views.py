from django.http import HttpResponse
from datetime import datetime
from . import views
from django.template import Context, Template, loader
import random
from home.models import DatosPersonales


def hola(request):
    return HttpResponse("Hola hola")


def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year-edad
    return HttpResponse(f'tu fecha de nacimiento aproximada para tus {edad} años es {fecha}')


def mi_index(request):

    cargar_archivo = open(
        r'C:\Users\Juan Carlos Diaz\Desktop\jcintermedio\templates\index.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)


def tu_template(request, nombre):

    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})

    return HttpResponse(template_renderizado)


def prueba_template(request):

    mi_contexto = {'rango': list(range(1, 11))}

    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)

    return HttpResponse(template_renderizado)


def crear_persona(request, nombre, apellido):

    persona = DatosPersonales(
        nombre=nombre, apellido=apellido, edad=random.randrange(1, 99))  # , fecha_nacimiento=datetime.now())
    persona.save()

    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'persona': persona})

    return HttpResponse(template_renderizado)


def ver_personas(request):
    # Persona es la BD, trae todos los objetos de la BD
    personas = DatosPersonales.objects.all()

    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})

    return HttpResponse(template_renderizado)
