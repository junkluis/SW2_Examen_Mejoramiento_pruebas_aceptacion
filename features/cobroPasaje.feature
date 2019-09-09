# language: es
# RUTA SUR= $0.35
Característica: Cobrar pasaje

 @jornadasDeIngreso

	Escenario: PRUEBA_ACEP_1
		Dado que tengo $20 dólares en mi carnet de codigo 201021755
		Cuando ponga mi carnet en el torniquete de la RUTA SUR y este si tenga Internet
		Entonces se descontará el pasaje según la ruta que escogí
		Y se presentará el nuevo saldo: $19.65

	Escenario: PRUEBA_ACEP_2
		Dado que tengo $0.25 dólares en mi carnet de codigo 201021755
		Cuando ponga mi carnet en el torniquete de la RUTA SUR y este si tenga Internet
		Entonces se mostrara el mensaje "No dispone de monto suficiente"
		Y se presentará el saldo: $0.25

