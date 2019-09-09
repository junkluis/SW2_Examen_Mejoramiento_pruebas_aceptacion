from behave import *
from src.cobrar_pasaje import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}
	
@given("Un carnet estudiantil con codigo '{codigo}'")
def step_impl(context,codigo):
	context.carnet_estudiantil={"codigo":codigo}

@given("un saldo {saldo}")
def step_impl(context,saldo):
	context.carnet_estudiantil={"saldo":saldo}

@given("un torniquete con conexion a internet '{conexion}'")
def step_impl(context,conexion):
	if conexion == 'activa':
		context.conexion=True
	else:
		context.conexion=False

@when("se solicite el cobrar pasaje en la ruta '{ruta}'")
def step_impl(context,ruta):
	context.ruta=ruta
	mensaje = cobrar_pasaje_ruta(context.ruta,context.carnet_estudiantil,context.conexion)
	context.mensaje =mensaje 


@then("se muestra el mensaje: {mensaje}")
def step_impl(context, mensaje):
	assert context.mensaje == mensaje
