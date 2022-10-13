from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import redirect, render, redirect
import random
from home.forms import HumanoFormulario, BusquedaHumanoFormulario

from home.models import DatosPersonales


# def hola(request):
#     return HttpResponse("Hola hola")


# def calcular_fecha_nacimiento(request, edad):
#     fecha = datetime.now().year-edad
#     return HttpResponse(f'tu fecha de nacimiento aproximada para tus {edad} años es {fecha}')


# def mi_index(request):

#     cargar_archivo = open(
#         r'C:\Users\Juan Carlos Diaz\Desktop\jcintermedio\home\templates\index.html', 'r')
#     template = Template(cargar_archivo.read())
#     cargar_archivo.close()

#     contexto = Context()
#     template_renderizado = template.render(contexto)
#     return HttpResponse(template_renderizado)


# def tu_template(request, nombre):

#     template = loader.get_template('home/tu_template.html')
#     template_renderizado = template.render({'persona': nombre})

#     return HttpResponse(template_renderizado)


def prueba_template(request):

    mi_contexto = {'rango': list(range(1, 11))}

    template = loader.get_template('home/prueba_template.html')
    template_renderizado = template.render(mi_contexto)

    return HttpResponse(template_renderizado)


# def crear_persona(request, nombre, apellido):

#     persona = DatosPersonales(
#         nombre=nombre, apellido=apellido, edad=random.randrange(1, 99))  # , fecha_nacimiento=datetime.now())
#     persona.save()

#     template = loader.get_template('crear_persona.html')
#     template_renderizado = template.render({'persona': persona})

#     return HttpResponse(template_renderizado)

# def crear_persona(request, nombre, apellido):

#     persona = DatosPersonales(
#         nombre=nombre, apellido=apellido, edad=random.randrange(1, 99))  # , fecha_nacimiento=datetime.now())
#     persona.save()

#     return render(request, 'home/crear_persona.html', {'persona': persona})

# def ver_personas(request):
#     # Persona es la BD, trae todos los objetos de la BD
#     personas = DatosPersonales.objects.all()

#     template = loader.get_template('ver_personas.html')
#     template_renderizado = template.render({'personas': personas})

#     return HttpResponse(template_renderizado)


# def ver_personas(request):
#     personas = DatosPersonales.objects.all()
#     return render(request, 'home/ver_personas.html', {'personas': personas})


def index(request):
    return render(request, 'home/index.html')


# def crear_persona(request):

#     if request.method == 'POST':

#         nombre = request.POST.get('nombre')
#         apellido = request.POST.get['nombre']
#         persona = DatosPersonales(
#             nombre=nombre, apellido=apellido, edad=random.radrange(1, 99))
#         persona.save()

#         return redirect('ver_persona')

#     formulario = HumanoFormulario()

#     return render(request, 'home/crear_persona.html', {'formulario': formulario})


def crear_persona(request):

    if request.method == 'POST':

        formulario = HumanoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data.get('fecha_creacion', datetime.now())

            persona = DatosPersonales(nombre=nombre, apellido=apellido,
                                      edad=edad)
            persona.save()

            return redirect('ver_personas')

    formulario = HumanoFormulario()

    return render(request, 'home/crear_persona.html', {'formulario': formulario})


def ver_personas(request):

    nombre = request.GET.get('nombre', None)

    if nombre:
        personas = DatosPersonales.objects.filter(nombre__icontains=nombre)
    else:
        personas = DatosPersonales.objects.all()

    formulario = BusquedaHumanoFormulario()

    return render(request, 'home/ver_personas.html', {'personas': personas, 'formulario': formulario})


def index(request):

    return render(request, 'home/index.html')
