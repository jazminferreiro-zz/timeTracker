from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django import forms
from django.urls import reverse

import simplejson as json
from datetime import datetime

from .forms import AddHoursForm

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
	context = {'desarrollador': desarrollador,'proyectos':proyectos, 'tareasPorProyecto':json.dumps(tareasPorProyecto),'error':False}
	return render(request, 'timeTracker/detail.html',context)

def add(request, desarrollador_id):
	desarrollador = get_object_or_404(Desarrollador, pk=desarrollador_id)

	if request.method == 'POST':
		#create a form instance and populate it with data from the request:
		print "En un POST"
		form = AddHoursForm(request.POST)
		#check whether it's valid:
		if form.is_valid():
        	#process the data in form.cleaned_data as required
			print "es validaaaaaaaa"
           	


			cantidad = int(request.POST['cantidad'])
			print "cantidad: " + str(cantidad)

			proyecto =  request.POST['proyecto'] 
			print "proyecto: " + proyecto

			tarea_index = int(request.POST['tarea'])
			global tareasPorProyecto
			tarea_name = tareasPorProyecto.get(proyecto)[tarea_index]
			print "tarea: "+ tarea_name
			tarea =  get_object_or_404(Tarea, nombre=tarea_name)

			fecha = request.POST['fecha']
			print "fecha: "+ fecha
			fecha = datetime.strptime(fecha, '%Y-%m-%d')
		

			#agrego horas
			desarrollador.horas_set.create( desarrollador = desarrollador, tarea = tarea, cantidad = cantidad, fecha = fecha)
			
			return HttpResponseRedirect(reverse('timeTracker:detail', args=(desarrollador.id,)))
		else:	
			print "no es valida"
			print form.errors.as_data()
			proyectos = Proyecto.objects.all()
			context = {'desarrollador': desarrollador,'proyectos':proyectos, 'tareasPorProyecto':json.dumps(tareasPorProyecto), 'error':True}
			return render(request, 'timeTracker/detail.html', context)

	#if a GET (or any other method) we'll create a blank form
	else:
		print "es un GET"






	"""print "tratando de sacar cantidad"
	
	cantidad = int(request.POST['cantidad'])


	print "cantidad: " + str(cantidad)


	try:
		proyecto =  request.POST['proyecto']
	except MultiValueDictKeyError:
		msg_error = "error de proyecto"
		print msg_error
		form.add_error(None, 'Please rate first')


	

	print "proyecto: " + proyecto.nombre

	tarea_index = int(request.POST['tarea'])

	global tareasPorProyecto
	tarea_name = tareasPorProyecto.get(proyecto)[tarea_index]

	print "tarea: "+ tarea_name
	tarea =  get_object_or_404(Tarea, nombre=tarea_name)

	fecha = request.POST['fecha']

	print "fecha: "+ fecha

	fecha = datetime.strptime(fecha, '%Y-%m-%d')

	#Guardo las horas
	desarrollador.horas_set.create( desarrollador = desarrollador, tarea = tarea, cantidad = cantidad, fecha = fecha)
	return HttpResponseRedirect(reverse('timeTracker:detail', args=(desarrollador.id, form)))"""
   

