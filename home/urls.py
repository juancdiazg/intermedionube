from django.urls import path

from home import views

urlpatterns = [
    path('', views.index),
    path('hola/', views.hola),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('mi-index/', views.mi_index),
    path('tu-template/<str:nombre>/', views.tu_template),
    path('prueba-template/', views.prueba_template),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    path('crear-persona1/', views.crear_persona),
    path('ver-personas/', views.ver_personas),
]
