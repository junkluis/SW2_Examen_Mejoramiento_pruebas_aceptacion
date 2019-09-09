"""Archivo de pruebas con behave"""

import behave
from src.cobrar_pasaje import cobrar_pasaje_ruta

@given("que dispongo de ${dolares} dólares en mi carnet de código {codigo}")
def saldo_codigo(context, dolares, codigo):

    """Función1 para pruebas"""

    carnet = {"codigo": codigo, "saldo":float(dolares)}
    context.carnet = carnet
    print(carnet)

@when("acerque mi carnet al torniquete de la ruta {ruta} y este {internet} tenga Internet")
def ruta_internet(context, ruta, internet):

    """Función2 para pruebas"""

    context.ruta = ruta
    context.internet = internet == "sí"

@then("se descontará el pasaje según la ruta que escogí")
def descontar_pasaje1(context):

    """Función3 para pruebas"""

    retorno = cobrar_pasaje_ruta(context.ruta, context.carnet, context.internet)
    assert retorno == context.carnet["saldo"]

@then("se presentará el saldo: ${saldo}")
def descontar_pasaje2(context, saldo):

    """Función4 para pruebas"""

    print(context.carnet)
    assert float(saldo) == context.carnet["saldo"]

@then('se me presentará el mensaje "{mensaje}"')
def mensaje_de_error(context, mensaje):

    """Función5 para pruebas"""

    retorno = cobrar_pasaje_ruta(context.ruta, context.carnet, context.internet)
    print(retorno)
    assert retorno == mensaje
