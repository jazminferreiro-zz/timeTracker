# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

class Tarea(models.Model):
	nombre = models.CharField(max_length=200)
	def __str__(self):
		return str(self.nombre)

class Proyecto(models.Model):
	nombre= models.CharField(max_length=200)
	tareas = models.ForeignKey(Tarea, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.nombre)


class Horas(models.Model):
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	fecha = models.DateTimeField(auto_now_add=True, blank=False)
	tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.cantidad)


class Desarrollador(models.Model):
	nombre = models.CharField(max_length=200)
	apellido= models.CharField(max_length=200)
	edad = models.IntegerField(validators=[MinValueValidator(0)])
	horas = models.ForeignKey(Horas, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre+' '+self.apellido







