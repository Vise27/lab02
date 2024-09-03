from django.shortcuts import render

def index(request):
    return render(request, 'lab02/formulario.html')

def calcular(request):
    numero1 = float(request.POST['numero1'])
    numero2 = float(request.POST['numero2'])
    operacion = request.POST['operacion']
    
    if operacion == 'suma':
        resultado = numero1 + numero2
    elif operacion == 'resta':
        resultado = numero1 - numero2
    elif operacion == 'multiplicacion':
        resultado = numero1 * numero2
    else:
        resultado = 'Operación no válida'
    
    context = {
        'titulo': "Resultado",
        'respuesta': resultado,
    }
    return render(request, 'lab02/respuesta.html', context)
