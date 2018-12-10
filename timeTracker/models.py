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


class Tarea(models.Model):
	nombre = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyecto, blank= True, null=True, on_delete=models.SET_NULL)

	def getNombre(self):
		return str(self.nombre)
	def getProyecto(self):
		return str(self.proyecto.getNombre())

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



	def getTareasPorProyecto(self):
		tareasPorProyecto = {}
		for proyecto in Proyecto.objects.all():
			tareas = []
			for tarea in proyecto.tarea_set.all():
				tareas.append(tarea.nombre)
			tareasPorProyecto[proyecto.nombre] = tareas
		return tareasPorProyecto


	def cargarHoras(self, cant, proyecto, tarea,fecha):
		try:
			cantidad = int(cant)
		except:
			return ValidationError("La cantidad de horas debe ser un valor positivo mayor a uno")
		
		if(proyecto == None or proyecto == ""):
			return ValidationError("El proyecto es obligatorio")

		try:
			tarea_index = int(tarea)
			tarea_name = self.getTareasPorProyecto()[proyecto][tarea_index]
			tarea =  Tarea.objects.get(nombre=tarea_name)
		except:
			return ValidationError("La tarea es obligatoria")

		try:
			fecha = datetime.strptime(fecha, '%Y-%m-%d')
		except:
			return ValidationError("La fecha es obligatoria")

		self.horas_set.create( desarrollador = self, tarea = tarea, cantidad = cantidad, fecha = fecha)
		return None

	def __str__(self):
		return self.nombre+' '+self.apellido

class Horas(models.Model):
	desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE, blank= True, null=True)
	tarea = models.ForeignKey(Tarea, on_delete=models.SET_NULL, blank= True, null=True)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	fecha = models.DateTimeField(auto_now_add=True, blank=False)


	def __str__(self):
		return 'Proyecto= ' + str(self.tarea.proyecto)+\
		', \nTarea= ' + str(self.tarea)+ \
		', \nDesarrollador = ' + str(self.desarrollador) +\
		', \nCantidad= ' + str(self.cantidad)+' hs'








