# language: es

Característica: Cobrar pasaje

 @jornadasDeIngreso
  Escenario: Pago exitoso
      Dado que dispongo de dinero asociado a mi carnet estudiantil
      Y el torniquete dispone de conexion a internet
      Cuando acerque mi carnet de ESPOL al torniquete
      Entonces se me descontara el pasaje
      Y me presentara '1.7'


@jornadasDeIngreso
  Escenario: Pago insuficiente
      Dado que no dispongo de dinero asociado a mi carnet estudiantil
      Y el torniquete dispone de conexion a internet
      Cuando acerque mi carnet de ESPOL al torniquete
      Entonces aparecera el siguiente mensaje 'No dispone del monto suficiente'
      Y me presentara '0'


