from behave import *
from src.cobrar_pasaje import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("se cumplen los requisitos")
def step_impl(context):
	pass

@when("ejecutar una accion")
def step_impl(context):
	pass

@then("genera el siguiente resultado '{variable}'")
def step_impl(context, variable):
	print(variable)
	pass

@then("tambien ocurre (si es necesario)")
def step_impl(context):
	pass

@given("que tengo ${dolares} dólares en mi carnet de codigo {codigo}")
def saldo_codigo(context, dolares, codigo):
	carnet = {"codigo": codigo, "saldo":float(dolares)}
	context.carnet = carnet
	print(carnet)

@when("ponga mi carnet en el torniquete de la RUTA {ruta} y este {internet} tenga Internet")
def ruta_internet(context, ruta, internet):
	context.ruta = ruta
	context.internet = internet == "si"

@then("se descontará el pasaje según la ruta que escogí")
def descontarPasaje(context):
	retorno = cobrar_pasaje_ruta(context.ruta, context.carnet, context.internet)
	assert retorno == context.carnet["saldo"]

@then("se presentará el nuevo saldo: ${saldo}")
def descontarPasaje(context, saldo):
	print(context.carnet)
	assert float(saldo) == context.carnet["saldo"]

@then('se mostrara el mensaje "{mensaje}"')
def mensajeDeError(context, mensaje):
	retorno = cobrar_pasaje_ruta(context.ruta, context.carnet, context.internet)
	print(retorno)
	assert retorno == mensaje

