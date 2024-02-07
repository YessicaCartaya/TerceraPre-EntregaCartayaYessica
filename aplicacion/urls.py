from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "home"),

    path('plantas/', plantas, name = "plantas"),
    path('planta_form/', plantasForm, name = "planta_form"),

    path('buscar/', buscar, name = "buscar"),
    path('buscarPlantas/', buscarPlantas, name = "buscarPlantas"),


    path('macetas/', macetas, name = "macetas"),
    path('maceta_form/', macetasForm, name = "maceta_form"),


    path('fertilizantes/', fertilizantes, name = "fertilizantes"),
    path('fertilizante_form/', fertilizantesForm, name = "fertilizante_form"),
 
]