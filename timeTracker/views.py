from django.shortcuts import get_object_or_404, render

from .models import Proyecto
from .models import Desarrollador

"""
def index(request):
    proyectos = Proyecto.objects.order_by('-nombre_proyecto')[:5]
    context = {'proyectos' : proyectos}
    return render(request, 'timeTracker/index.html', context)

def verTareas (request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'timeTracker/verTareas.html', {'proyecto': proyecto})

def verHoras (request, question_id):
	response = "Estas viendo las horas del desarrollador %s."
	return HttpResponse(response % desarrollador_id)
"""

def index(request):
    desarrolladores = Desarrollador.objects.all()
    context = {'desarrolladores' : desarrolladores}
    return render(request, 'timeTracker/index.html', context)

def detail(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	return render(request, 'timeTracker/detail.html', {'desarrollador': desarrollador})



