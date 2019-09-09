# language: es

Característica: Cobrar pasaje

 @jornadasDeIngreso
  Escenario: Nombre del escenario
      Dado que se cumplen los requisitos
      Cuando se ejecute una accion
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)

	Escenario: CA1
		Dado que dispongo de $20 dólares en mi carnet de código 201417510
		Cuando acerque mi carnet al torniquete de la ruta DURAN y este sí tenga Internet
		Entonces se descontará el pasaje según la ruta que escogí
		Y se presentará el nuevo saldo: $19.50

	