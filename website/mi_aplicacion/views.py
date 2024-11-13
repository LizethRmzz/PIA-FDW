from django.shortcuts import render

def index(request):
    return render(request, 'mi_aplicacion/index.html')

def habitat(request):
    return render(request, 'mi_aplicacion/habitat.html')

def comportamiento(request):
    return render(request, 'mi_aplicacion/comportamiento.html')

def impacto(request):
    return render(request, 'mi_aplicacion/impacto.html')

def formulario(request):
    return render(request, 'mi_aplicacion/formulario.html')
