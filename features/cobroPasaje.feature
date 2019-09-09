# language: es
Característica: Cobrar pasaje

 @pagoConTarjeta
  Escenario: Saldo cobrado y actualizado correctamente
      Dado Un carnet estudiantil con codigo '0123456', con saldo '25', y el torniquete con conexion a internet 'activa'
      Cuando se solicite el cobrar pasaje en la ruta 'Norte'
      Entonces se muestra el mensaje: '24.70'

@pagoConTarjeta
  Escenario: Saldo insuficiente
      Dado Un carnet estudiantil con codigo '0123456', con saldo '0.10', y el torniquete con conexion a internet 'activa'
      Cuando se solicite el cobrar pasaje en la ruta 'Norte'
      Entonces se muestra el mensaje: 'Error: No dispone de monto suficiente'
