# from behave import *
# from src.cobrar_pasaje import *


#Condiciones antes de empezar cualquier STEP 
# def before_scenario(context, scenario):
# 	context = {}


# @given("que se cumplen los requisitos")
# def step_impl(context):
# 	pass

# @when("se ejecute una accion")
# def step_impl(context):
# 	pass

# @then("genera el siguiete resultado '{variable}'")
# def step_impl(context, variable):
# 	print(variable)
# 	pass

# @then("tambien ocurre lo siguiente (si es necesario)")
# def step_impl(context):
# 	pass

# language: es

Característica: Cobrar pasaje

 @jornadasDeIngreso
  Escenario: Nombre del escenario
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)

	Escenario: PRUEBA_ACEP_1
		Dado que tengo $20 dólares en mi carnet de código 201021755
		Cuando ponga mi carnet en el torniquete de la RUTA SUR y este tenga Internet
		Entonces se descontará el pasaje según la ruta que escogí
		Y se presentará el nuevo saldo: $19.65

	