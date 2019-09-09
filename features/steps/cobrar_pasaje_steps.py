from behave import *
from src.cobrar_pasaje import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que se tiene '{saldo}' dolares asociados al carnet estudiantil con codigo '{codigo}'")
def step_impl(context, saldo, codigo):
	carnet = {"codigo": int(codigo), "saldo": float(saldo)}
	context.carnet= carnet


@given("se tiene conexión a internet")
def step_impl(context):
    context.conexion = True

@when("se acerque el carnet al torniquete")
def step_impl(context):
	ruta = "NORTE"
	result = cobrar_pasaje_ruta(ruta, context.carnet, context.conexion)
	context.result = result

@then("se descontará el costo del pasaje")
def step_impl(context):
	pass

@then("mostara el mensaje: '{mensaje}'")
def step_impl(context, mensaje):
	print(context.result)
	assert(mensaje == context.result)

@then("se mostrará el siguiente costo actualizado : '{monto}'")
def step_impl(context, monto):
	assert(float(monto) == context.result)

@then("se mostrará el siguiente saldo actual : '{monto}'")
def step_impl(context, monto):
	assert(float(monto) == context.carnet["saldo"])