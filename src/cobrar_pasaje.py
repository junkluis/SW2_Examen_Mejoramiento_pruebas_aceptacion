"""Funciones necesarias para busqueda de peliculas."""

RUTAS = {
    "NORTE": {"valor": 0.30, "pasajeros":[]},
    "SUR": {"valor": 0.35, "pasajeros":[]},
    "CENTRO": {"valor": 0.25, "pasajeros":[]},
    "DURAN": {"valor": 0.50, "pasajeros":[]}
}

#carnet_luis={"codigo":000000000, "saldo":20}


def cobrar_pasaje_ruta(ruta_seleccionada, carnet_estudiantil, conexion_internet=True):
	'''Comentario'''
    if conexion_internet:
        ruta = RUTAS[ruta_seleccionada]
        if(carnet_estudiantil["codigo"] in ruta["pasajeros"]):
            mensaje_error = "Error: Este carnet aparece como duplicado"
            return (mensaje_error, carnet_estudiantil["saldo"])
        else:
            if carnet_estudiantil["saldo"] >= ruta["valor"]:
                nuevo_saldo = round(carnet_estudiantil["saldo"] - ruta["valor"], 2)
                carnet_estudiantil["saldo"] = nuevo_saldo
                ruta["pasajeros"].append(carnet_estudiantil["codigo"])
                return nuevo_saldo
            else:
                mensaje_error = "Error: No dispone de monto suficiente"
                return mensaje_error
    else:
        mensaje_error = "Error: No dispone de conexión a internet"
        return mensaje_error
