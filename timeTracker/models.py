# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

class Proyecto(models.Model):
	nombre= models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class Tarea(models.Model):
	nombre = models.CharField(max_length=200)
	proyecto = models.ForeignKey(Proyecto, blank= True, null=True, on_delete=models.SET_NULL)
	def __str__(self):
		return self.nombre


class Desarrollador(models.Model):
	nombre = models.CharField(max_length=200)
	apellido= models.CharField(max_length=200)
	edad = models.IntegerField(validators=[MinValueValidator(0)])
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







