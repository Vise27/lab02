from django.urls import path
from . import views

app_name = 't02'

urlpatterns = [
    path('', views.index, name='index'),
    path('calcular_volumen', views.calcular_volumen, name='calcular_volumen'),
]
