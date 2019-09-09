from behave import *
from src.cobrar_pasaje import *


# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}


@given("que dispongo de dinero asociado a mi carnet estudiantil")
def step_impl(context):
    student_id = {
        'codigo': '201505935',
        'saldo': 2
    }
    context.student_id = student_id


@given("que no dispongo de dinero asociado a mi carnet estudiantil")
def step_impl(context):
    student_id = {
        'codigo': '201505935',
        'saldo': 0
    }
    context.student_id = student_id


@given("el torniquete dispone de conexion a internet")
def step_impl(context):
    context.conection = True


@when("acerque mi carnet de ESPOL al torniquete")
def step_impl(context):
    if context.student_id['saldo'] >= 2:
        actual_balance = cobrar_pasaje_ruta(
            'NORTE', context.student_id, context.conection)
        context.actual_balance = actual_balance
    else:
        error_msg = cobrar_pasaje_ruta(
            'NORTE', context.student_id, context.conection)
        context.error_msg = error_msg


@then("genera el siguiete resultado '{variable}'")
def step_impl(context, variable):
    print(variable)
    pass


@then("se me descontara el pasaje")
def step_impl(context):
    pass


@then("me presentara '{actual_balance}'")
def step_impl(context, actual_balance):
    if str(context.scenario) == "Pago exitoso":
        assert(context.actual_balance, float(actual_balance))
    elif str(context.scenario) == "Pago insuficiente":
        assert(context.student_id['saldo'], float(actual_balance))


@then("aparecera el siguiente mensaje '{msg}'")
def step_impl(context, msg):
    assert(context.error_msg, msg)
