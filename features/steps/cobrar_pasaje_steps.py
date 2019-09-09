"""Modulo steps para puebas de behave"""
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
        resultado = list(cobrar_pasaje_ruta(context.ruta,
                                        context.carnet,
                                        context.conexion))
        if len(resultado) == 1 and type(resultado[0]) == int:
            context.saldo = resultado[0]
        elif len(resultado) == 2:
            context.mensaje = resultado[0]
            context.saldo = resultado[1]
        else:
            context.mensaje = resultado[0]


@then("se debita de mi saldo en base a mi ruta")
def step_impl(context):
        """ actualiza el saldo del carnet """
        assert(type(context.saldo) == float)
        context.carnet['saldo'] = context.saldo


@then("se me muestra mi saldo como ${saldo}")
def step_impl(context, saldo):
        """ se muestra el resultado de la transaccion"""
        assert(context.carnet['saldo'] == float(saldo))
        print("Su saldo es $%s" % saldo)


@then("se me muestra el mensaje {mensaje}")
def step_impl(context, mensaje):
        """ se muestra el resultado de la transaccion"""
        assert(context.mensaje == mensaje)
