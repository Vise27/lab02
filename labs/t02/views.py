from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 't02/calculadora_cilindro.html')

def calcular_volumen(request):
    altura = float(request.POST['altura'])
    diametro = float(request.POST['diametro'])
    radio = diametro / 2
    volumen = 3.1416 * (radio ** 2) * altura 
    
    context = {
        'titulo': "Resultado del Volumen",
        'volumen': volumen,
    }
    return render(request, 't02/resultado_volumen.html', context)
