from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('hola/', views.hola, name='hola'),
    # path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento,         name='calcular_fecha_nacimiento'),
    # path('mi-index/', views.mi_index, name='mi_index'),
    # path('tu-template/<str:nombre>/', views.tu_template, name='tu_template'),
    path('prueba-template/', views.prueba_template, name='prueba_template'),
    path('crear-persona/', views.crear_persona, name='crear_persona'),
    path('ver-personas/', views.ver_personas, name='ver_personas'),

]
