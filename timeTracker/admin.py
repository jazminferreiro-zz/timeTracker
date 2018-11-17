# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Proyecto, Tarea, Desarrollador, Horas

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Tarea)
admin.site.register(Horas)
admin.site.register(Desarrollador)
