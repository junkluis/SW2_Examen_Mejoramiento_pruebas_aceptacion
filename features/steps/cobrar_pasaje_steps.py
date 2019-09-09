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



@given("que dispongo dinero asociado a mi'{carnet_estudiantil}'")
def step_impl(context, carnet_estudiantil):
	context.carnet_estudiantil = carnet_estudiantil


@given("dispone de conexion a internet'{conexion_internet}'")
def step_impl(context, conexion_internet):
	context.conexion_internet = conexion_internet

@when("acerque mi carnet estudiantil {carnet_estudiantil}")
def step_impl(context, ruta):



@then("se me descontara el pasaje segun la ruta {ruta}")
def step_impl(context,conexion_internet,ruta_seleccionada,carnet_estudiantil):
	context.conexion_internet= conexion_internet
	context.carnet_estudiantil= carnet_estudiantil
	context.ruta_seleccionada= ruta_seleccionada
	nuevo_saldo =cobrar_pasaje_ruta(ruta_seleccionada, carnet_estudiantil, conexion_internet=True)
	print nuevo_saldo



