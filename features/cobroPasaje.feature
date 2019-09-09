# language: es

Característica: Cobrar pasaje

 @dineroSuficiente
  Escenario: pagar pasaje con suficiente saldo
      Dado que se tiene '2' dolares asociados al carnet estudiantil con codigo '00000'
      Y se tiene conexión a internet
      Cuando se acerque el carnet al torniquete
      Entonces se descontará el costo del pasaje
      Y se mostrará el siguiente costo actualizado : '1.70'

 @dineroInsuficiente
  Escenario: pagar pasaje sin suficiente saldo
      Dado que se tiene '0.1' dolares asociados al carnet estudiantil con codigo '00001'
      Y se tiene conexión a internet
      Cuando se acerque el carnet al torniquete
      Entonces mostara el mensaje: 'Error: No dispone de monto suficiente'
      Y se mostrará el siguiente saldo actual : '0.1'
