from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import simplejson as json

from .models import Proyecto
from .models import Tarea
from .models import Desarrollador


def index(request):
    desarrolladores = Desarrollador.objects.all()
    context = {'desarrolladores' : desarrolladores}
    return render(request, 'timeTracker/index.html', context)

def detail(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	proyectos = Proyecto.objects.all()
	dic = {}
	for proyecto in Proyecto.objects.all():
		tareas = []
		for tarea in proyecto.tarea_set.all():
			tareas.append(tarea.nombre)
		dic[proyecto.nombre] = tareas

	dicPrueba = {'val1' : 'this is x', 'val2' : True}

	context = {'desarrollador': desarrollador,'proyectos':proyectos, 'tareasPorProyecto':json.dumps(dic)}
	return render(request, 'timeTracker/detail.html',context)

def add(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	proyecto =request.POST['proyecto']
	cantidad = request.POST['cantidad']
	print proyecto	
	print cantidad
	return HttpResponseRedirect(reverse('timeTracker:detail', args=(desarrollador.id,)))
   

