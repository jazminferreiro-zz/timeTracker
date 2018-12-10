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
	context.model = Desarrollador(nombre="juan",apellido = "code",edad= "55");
	

@when('we add hour')
def step_impl(context):
	proyecto = Proyecto(nombre= "p1")
	context.model.cargarHoras(5, proyecto, 0, "20/12/2016")

@then('we will find an hour created')
def step_impl(context):
	assert context.failed is False

#############################################################

@when('we try to add hours with black project')
def step_impl(context):
	context.exc = context.model.cargarHoras(5, "", 0, "20/12/2016")
	
@when('we try to add hours with not project')
def step_impl(context):
	context.exc = context.model.cargarHoras(5, None, 0, "20/12/2016")
	

#############################################################

@when('we try to add more than 24 hours')
def step_impl(context):
	context.exc = context.model.cargarHoras(5, "p1",0, 25, "20/12/2016")


#############################################################
	
@then('it throws a ValidationError with message "{msg}"')
def step_impl(context, msg):
	print context.exc.msg
	assert (context.exc.msg == msg) is True

#############################################################

