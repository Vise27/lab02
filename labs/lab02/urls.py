from django.urls import path
from . import views

app_name = 'lab02'

urlpatterns = [
    path('', views.index, name='index'),
    path('calcular', views.calcular, name='calcular'),
]