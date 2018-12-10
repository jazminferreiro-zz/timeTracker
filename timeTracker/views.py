from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django import forms
from django.urls import reverse

import simplejson as json



from .models import *

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





def renderDetail(request, desarrollador_id, errors):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	fillGlobalDictionary()
	global tareasPorProyecto
	proyectos = Proyecto.objects.all()
	context = {'desarrollador': desarrollador,'proyectos':proyectos, 'tareasPorProyecto':json.dumps(tareasPorProyecto), 'errors': errors}
	return render(request, 'timeTracker/detail.html', context)



def index(request):
    desarrolladores = Desarrollador.objects.all()
    context = {'desarrolladores' : desarrolladores}
    return render(request, 'timeTracker/index.html', context)

def detail(request, desarrollador_id):
	return renderDetail(request, desarrollador_id, [])

def add(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)
	cantidad = request.POST.get('cantidad',None)
	proyecto =  request.POST.get('proyecto', None)
	tarea_index = request.POST.get('tarea', None)
	fecha = request.POST.get('fecha', None)

	global tareasPorProyecto

	validationError = desarrollador.cargarHoras(cantidad, proyecto, tarea_index, fecha, tareasPorProyecto, Tarea.objects.all())
	if(validationError == None):
		return HttpResponseRedirect(reverse('timeTracker:detail', args=(desarrollador.id,)))
	else:
		return renderDetail(request, desarrollador_id,[validationError.msg])
		
			
		
			


