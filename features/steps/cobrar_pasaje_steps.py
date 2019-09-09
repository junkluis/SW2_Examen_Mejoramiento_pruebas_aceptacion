from behave import *
from src.cobrar_pasaje import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que se cumplen los requisitos")
def step_impl(context):
	pass

@when("se ejecute una accion")
def step_impl(context):
	pass

@then("genera el siguiete resultado '{variable}'")
def step_impl(context, variable):
	print(variable)
	pass

@then("tambien ocurre lo siguiente (si es necesario)")
def step_impl(context):
	pass

@given("que dispongo de ${dolares} dólares en mi carnet de código {codigo}")
def saldo_codigo(context, dolares, codigo):
	carnet = {"codigo": codigo, "saldo":float(dolares)}
	context.carnet = carnet
	print(carnet)

@when("acerque mi carnet al torniquete de la ruta {ruta} y este {internet} tenga Internet")
def ruta_internet(context, ruta, internet):
	context.ruta = ruta
	context.internet = internet == "sí"

@then("se descontará el pasaje según la ruta que escogí")
def descontarPasaje(context):
	retorno = cobrar_pasaje_ruta(context.ruta, context.carnet, context.internet)
	assert retorno == context.carnet["saldo"]

@then("se presentará el saldo: ${saldo}")
def descontarPasaje(context, saldo):
	print(context.carnet)
	assert float(saldo) == context.carnet["saldo"]

@then('se me presentará el mensaje "{mensaje}"')
def mensajeDeError(context, mensaje):
	retorno = cobrar_pasaje_ruta(context.ruta, context.carnet, context.internet)
	print(retorno)
	assert retorno == mensaje

