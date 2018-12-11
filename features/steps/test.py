from behave import *

from django.conf import settings


from timeTracker.models import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
	assert context.failed is False

#############################################################
@given('a project with name p1')
def step_impl(context):
    context.model = Proyecto(nombre= "p1")

@when('we look for the name')
def step_impl(context):
	context.exc = context.model.getNombre()

@then('it is p1')
def step_impl(context):
	assert (context.exc == "p1") is True

#############################################################

@given('a task with name t1 and project name p1')
def step_impl(context):
    proyecto = Proyecto(nombre= "p1")
    context.model = Tarea(nombre= "t1", proyecto = proyecto)

@when('we look for the task name')
def step_impl(context):
	context.exc = context.model.getProyecto()

@then('it is t1')
def step_impl(context):
	assert (context.exc == "p1") is True

#############################################################

@given('a set of project')
def step_impl(context):
	model = getattr(context, "model", None)
	if not model:
		context.model = {}
	for row in context.table:
		proyecto = Proyecto(nombre= row["proyecto"])
		tarea = Tarea(nombre = row["tarea"],proyecto = proyecto)
		context.model[row["tarea"]]= tarea

	
@when('nothing happens')
def step_impl(context):
	assert True is not False

@then('we will find that "{nombre_tarea}" belongs to the proyecto: "{nombre_proyecto}"')
def step_impl(context, nombre_tarea, nombre_proyecto):
	tarea = context.model[nombre_tarea]
	assert (tarea.getProyecto()== nombre_proyecto) is True

#############################################################

@given('a developer')
def step_impl(context):
	context.model = Desarrollador.objects.create(nombre="juan",apellido = "code",edad= "55");
	

#############################################################


@when('we try to add hours with black project')
def step_impl(context):
	context.exc = context.model.cargarHoras(5, "", 0, "2016-12-29", {}, [])
	
@when('we try to add hours with not project')
def step_impl(context):
	context.exc = context.model.cargarHoras(5, None, 0, "2016-12-29",{}, [])
	

#############################################################

@when('we try to add a not integer quantity value')
def step_impl(context):
	context.exc = context.model.cargarHoras("cinco", "p1", 0, "2016-12-29",{}, [])


#############################################################

@when('we try to add more than 24 hours')
def step_impl(context):
	context.exc = context.model.cargarHoras(25, "p1",0, "2016-12-29",{}, [])


#############################################################


@when('we try to we try to add hours vith no date')
def step_impl(context):
	context.exc = context.model.cargarHoras(2, "p1",0, None,{}, [])


#############################################################

@when('we try to add hours vith invalid date format')
def step_impl(context):
	context.exc = context.model.cargarHoras(2, "p1",0, "34 de noviembre de 2018",{}, [])


#############################################################

@when('we try to add hours vith None task index')
def step_impl(context):
	context.exc = context.model.cargarHoras(2, "p1",None, "2016-12-29",{}, [])


#############################################################

@when('we try to add hours vith invalid task index')
def step_impl(context):
	context.exc = context.model.cargarHoras(2, "p1",0, "2016-12-29",{}, [])

#############################################################

@when('we try to add hours to a task we are not assigned to')
def step_impl(context):
	otroDesarrollador = Desarrollador.objects.create(nombre="Lala",apellido = "Lelo",edad= "55")
	proyecto1 = Proyecto.objects.create(nombre="proyecto1")
	tarea0 = Tarea.objects.create(nombre ="tarea0",proyecto = proyecto1, responsable = otroDesarrollador)

	tareasPorProyectos = {}
	tareasPorProyectos["proyecto1"] = ["tarea0"]
	tareas = [tarea0]

	context.exc = context.model.cargarHoras(2, "proyecto1",0, "2016-12-29",tareasPorProyectos, tareas)

#############################################################
@then('it throws a ValidationError with message "{msg}"')
def step_impl(context, msg):
	print context.exc.msg
	assert (context.exc.msg == msg) is True

#############################################################
@when('we try to add hour with invalid task')
def step_impl(context):
	proyecto1 = Proyecto(nombre="proyecto1")
	tarea0 = Tarea(nombre ="tarea0",proyecto = proyecto1)

	proyecto2 = Proyecto(nombre="proyecto2")
	tarea1 = Tarea(nombre ="tarea1",proyecto = proyecto2)
	tareasPorProyectos = {}
	tareasPorProyectos["proyecto1"] = ["tarea3"]
	tareasPorProyectos["proyecto2"] = ["tarea1"]
	tareas = [tarea0, tarea1]

	context.exc = context.model.cargarHoras(2, "proyecto1",0, "2016-12-29",tareasPorProyectos, tareas)
	print context.exc.msg

#############################################################

@when('we add hour')
def step_impl(context):
	proyecto1 = Proyecto.objects.create(nombre="proyecto1")
	tarea0 = Tarea.objects.create(nombre ="tarea0",proyecto = proyecto1, responsable = context.model)

	proyecto2 = Proyecto.objects.create(nombre="proyecto2")
	tarea1 = Tarea.objects.create(nombre ="tarea1",proyecto = proyecto2, responsable = context.model)
	tareasPorProyectos = {}
	tareasPorProyectos["proyecto1"] = ["tarea0"]
	tareasPorProyectos["proyecto2"] = ["tarea1"]
	tareas = [tarea0, tarea1]

	context.exc = context.model.cargarHoras(2, "proyecto1",0, "2016-12-29",tareasPorProyectos, tareas)


@then('we will find an hour created')
def step_impl(context):
	assert context.failed is False
	assert (context.exc == None) is True

#############################################################



