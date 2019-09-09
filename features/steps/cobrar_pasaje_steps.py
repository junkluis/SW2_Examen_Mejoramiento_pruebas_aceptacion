from behave import *
from src.cobrar_pasaje import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
        """ Settear el contexto necesario a tener para cada escenario"""        
        context = {}


@given("dispongo de mi carnet de estudiante con codigo {codigo} y ${saldo} saldo")
def step_impl(context, codigo, saldo):
        """Llena la informacion relevante del carnet estudiantil"""        
        context.carnet = {}
        context.carnet["codigo"] = codigo
        context.carnet["saldo"] = float(saldo)

@given("estoy tomando la ruta {ruta}")
def step_impl(context, ruta):
        """ especifica la ruta tomada """
        context.ruta = ruta


@given("el torniquete {conexion} tiene conexion a internet")
def step_impl(context, conexion):
        """ indica si hay conextion a internet para el torniquete """
        conexion = conexion.lower()
        if conexion == "si":
            context.conexion = True
        elif conexion == "no":
            context.conexion = False
        else:
            conexion = None
        assert(conexion != None)


@when("pase el carnet por el torniquete")
def step_impl(context):
        """ realiza el cobro de saldo """
        resultado = cobrar_pasaje_ruta(context.ruta,
                                        context.carnet,
                                        context.conexion)
        context.resultado = resultado


@then("se debita de mi saldo en base a mi ruta")
def step_impl(context):
        """ actualiza el saldo del carnet """
        assert(type(context.resultado) == float)
        context.carnet['saldo'] = context.resultado


@then("se me muestra mi saldo restante como ${saldo_restante}")
def step_impl(context, saldo_restante):
        """ se muestra el resultado de la transaccion"""
        assert(context.carnet['saldo'] == float(saldo_restante))
        print("Su saldo es $%s" % saldo_restante)
