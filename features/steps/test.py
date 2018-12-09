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


@given('a set of project')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = []
    for row in context.table:
    	proyecto = Proyecto(row["proyecto"])
    	tarea = Tarea(row["tarea"], proyecto=proyecto)


@when('we hacemos algo')
def step_impl(context):
    assert True is not False

@then('we will find el proyecto "{proyecto}"')
def step_impl(context, proyecto):
    assert context.failed is False





