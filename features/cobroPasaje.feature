# language: es

Característica: Cobrar pasaje

 @jornadasDeIngreso

	Escenario: CA1
		Dado que dispongo de $20 dólares en mi carnet de código 201417510
		Cuando acerque mi carnet al torniquete de la ruta DURAN y este sí tenga Internet
		Entonces se descontará el pasaje según la ruta que escogí
		Y se presentará el saldo: $19.50

	Escenario: CA2
		Dado que dispongo de $0.25 dólares en mi carnet de código 201417511
		Cuando acerque mi carnet al torniquete de la ruta DURAN y este sí tenga Internet
		Entonces se me presentará el mensaje "Error: No dispone de monto suficiente"
		Y se presentará el saldo: $0.25