# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Proyecto(models.Model):
	nombre= models.CharField(max_length=200)
	def getNombre(self):
		return str(self.nombre)

class ValidationError:

	def __init__(self, msg):
		self.msg = msg

	def __eq__(self, other):
		"""Overrides the default implementation"""
		if isinstance(other, ValidationError):
			return self.msg == other.msg
		return False


class Desarrollador(models.Model):
	nombre = models.CharField(max_length=200)
	apellido= models.CharField(max_length=200)
	edad = models.IntegerField(validators=[MinValueValidator(0)])

	def buscarTarea(self, tareas, tarea_name):
		for tarea in tareas:
			if(tarea.nombre == tarea_name):
				return tarea
		return None

	def cargarHoras(self, cant, proyecto, tarea,fecha, tareasPorProyecto, tareas):
		try:
			cantidad = int(cant)
		except:
			return ValidationError("La cantidad de horas debe ser un valor positivo mayor a uno")
		if(cantidad > 24):
			return ValidationError("La cantidad de horas debe ser menor a 24")

		if(proyecto == None or proyecto == ""):
			return ValidationError("El proyecto es obligatorio")

		try:
			fecha = datetime.strptime(fecha, '%Y-%m-%d')
		except:
			return ValidationError("La fecha es obligatoria")
		
		try:
			tarea_index = int(tarea)
			tarea_name = tareasPorProyecto[proyecto][tarea_index]
		except:
			return ValidationError("La tarea es obligatoria")
		
		tarea =  self.buscarTarea(tareas, tarea_name)
		if(tarea == None):
			return ValidationError("La tarea: "+tarea_name+ " no esta disponible")
		if(tarea.responsable != self):
			return ValidationError("La tarea: "+tarea_name+ " no esta a cargo de este desarrollador")
		horasTrabajadas = 0
		for hora in self.horas_set.all() :
			if (hora.tarea == tarea and hora.fecha.date() == fecha.date()):
				horasTrabajadas += hora.cantidad
		if (horasTrabajadas+cantidad > 24 ):
			return ValidationError("La cantidad de horas cargadas por dia para una tarea debe ser menor o igual a 24")
		
		self.horas_set.create( desarrollador = self, tarea = tarea, cantidad = cantidad, fecha = fecha)
		return None

	def __str__(self):
		return self.nombre+' '+self.apellido

class Tarea(models.Model):
	nombre = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyecto, blank= True, null=True, on_delete=models.SET_NULL)
	responsable = models.ForeignKey(Desarrollador, blank= True, null=True, on_delete=models.SET_NULL)
	def getNombre(self):
		return str(self.nombre)
	def getProyecto(self):
		return str(self.proyecto.getNombre())

class Horas(models.Model):
	desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE, blank= True, null=True)
	tarea = models.ForeignKey(Tarea, on_delete=models.SET_NULL, blank= True, null=True)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	fecha = models.DateTimeField(auto_now_add=False, blank=False)


	def __str__(self):
		return 'Proyecto= ' + str(self.tarea.proyecto)+\
		', \nTarea= ' + str(self.tarea)+ \
		', \nDesarrollador = ' + str(self.desarrollador) +\
		', \nCantidad= ' + str(self.cantidad)+' hs'








