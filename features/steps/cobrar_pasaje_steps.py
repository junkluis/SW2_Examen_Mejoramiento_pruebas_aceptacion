from behave import *
from src.cobrar_pasaje import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

@given("soy estudiante de ESPOL con carnet en la ruta {ruta_viaje}"):
def step_impl(context, carnet):
	context.carnet_estudiantil = {"codigo":000000000, "saldo":20}
	context.ruta_viaje = ruta_viaje

@given("que dispongo de {total_saldo} en mi carnet estudiantil y el torniquete dispone de conexión a internet")
def step_impl(context, total_saldo):
	context.total_saldo = total_saldo

@when("acerque mi carnet de ESPOL al torniquete")
def step_impl(context):
	if context.ruta_viaje == "NORTE":
		ruta_seleccionada = "NORTE"
		carnet_estudiantil = context.carnet_estudiantil
		mensaje_error = cobrar_pasaje_ruta(ruta_seleccionada, carnet_estudiantil)
		context.mensaje_error = mensaje_error

@then("se me escontará '{variable}'")
def step_impl(context, variable):
	print(variable)
	context.total_saldo = context.total_saldo - variable

@then("me presentará el mensaje: {mensaje_error}")
def step_impl(context, mensaje):
	assert context.mensaje_error == mensaje