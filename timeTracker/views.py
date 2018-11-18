from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import simplejson as json

from .models import Proyecto
from .models import Tarea
from .models import Desarrollador


def tareasPorProyecto():
	dic = {}
	for proyecto in Proyecto.objects.all():
		tareas = []
		for tarea in proyecto.tarea_set.all():
			tareas.append(tarea.nombre)
		dic[proyecto.nombre] = tareas
	return dic;


def index(request):
    desarrolladores = Desarrollador.objects.all()
    context = {'desarrolladores' : desarrolladores}
    return render(request, 'timeTracker/index.html', context)

def detail(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	proyectos = Proyecto.objects.all()
	dic = tareasPorProyecto()
	context = {'desarrollador': desarrollador,'proyectos':proyectos, 'tareasPorProyecto':json.dumps(dic)}
	return render(request, 'timeTracker/detail.html',context)

def add(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	
	cantidad = int(request.POST['cantidad'])

	print request.POST['proyecto']
	#print Proyecto.objects.all().get(pk=request.POST['proyecto'])	
	
	
	print cantidad
	dic = tareasPorProyecto()
	tarea_index = int(request.POST['tarea'])
	tareas = dic.get(proyecto)
	tarea = tareas[tarea_index]
	print tarea

	#print desarrollador.horas_set.create( cantidad = cantidad, proyecto = proyecto )
	return HttpResponseRedirect(reverse('timeTracker:detail', args=(desarrollador.id,)))
   

