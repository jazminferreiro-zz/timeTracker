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
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre

class Horas(models.Model):
	fecha = models.DateTimeField(auto_now_add=True, blank=False)
	tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	def __str__(self):
		return str(self.cantidad)


class Desarrollador(models.Model):
	nombre = models.CharField(max_length=200)
	apellido= models.CharField(max_length=200)
	edad = models.IntegerField(validators=[MinValueValidator(0)])
	horas = models.ForeignKey(Horas, blank=True, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre+' '+self.apellido







