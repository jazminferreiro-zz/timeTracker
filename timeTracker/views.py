from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import simplejson as json
from datetime import datetime

from .models import Proyecto
from .models import Tarea
from .models import Desarrollador
from .models import Horas



tareasPorProyecto = None

def fillGlobalDictionary():
	global tareasPorProyecto
	tareasPorProyecto = {}
	for proyecto in Proyecto.objects.all():
		tareas = []
		for tarea in proyecto.tarea_set.all():
			tareas.append(tarea.nombre)
		tareasPorProyecto[proyecto.nombre] = tareas
	return tareasPorProyecto;



def index(request):
    desarrolladores = Desarrollador.objects.all()
    context = {'desarrolladores' : desarrolladores}
    return render(request, 'timeTracker/index.html', context)

def detail(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	proyectos = Proyecto.objects.all()
	fillGlobalDictionary()
	global tareasPorProyecto
	context = {'desarrollador': desarrollador,'proyectos':proyectos, 'tareasPorProyecto':json.dumps(tareasPorProyecto)}
	return render(request, 'timeTracker/detail.html',context)

def add(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	
	cantidad = int(request.POST['cantidad'])

	proyecto =  request.POST['proyecto']

	tarea_index = int(request.POST['tarea'])
	global tareasPorProyecto
	tarea_name = tareasPorProyecto.get(proyecto)[tarea_index]
	tarea =  get_object_or_404(Tarea, nombre=tarea_name)

	fecha = request.POST['fecha']
	fecha = datetime.strptime(fecha, '%Y-%m-%d')

	#Guardo las horas
	desarrollador.horas_set.create( desarrollador = desarrollador, tarea = tarea, cantidad = cantidad, fecha = fecha)
	return HttpResponseRedirect(reverse('timeTracker:detail', args=(desarrollador.id,)))
   

