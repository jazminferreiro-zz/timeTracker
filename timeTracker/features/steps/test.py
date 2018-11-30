from behave import *


@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


@given('I search for a valid account')
def step_impl(context):
    context.browser.get('http://localhost:8000/index')
    form = find_element_by_link_text("Iniciar sesion").click()

@then('I will see the account details')
def step_impl(context):
    elements = find_elements(context.browser, id='tareasSelect')
   