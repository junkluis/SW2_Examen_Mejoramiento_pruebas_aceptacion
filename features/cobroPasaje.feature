# language: es

Característica: Cobrar pasaje

 @jornadasDeIngreso
  Escenario: Pago de pasaje exitoso
      Dado dispongo de mi carnet de estudiante con codigo 201414466 y $0.75 saldo
      Y estoy tomando la ruta CENTRO
      Y el torniquete si tiene conexion a internet
      Cuando pase el carnet por el torniquete
      Entonces se debita de mi saldo en base a mi ruta
      Y se me muestra mi saldo como $0.50


 @jornadasDeIngreso
  Escenario: Pago de pasaje exitoso
      Dado dispongo de mi carnet de estudiante con codigo 201414466 y $0.15 saldo
      Y estoy tomando la ruta CENTRO
      Y el torniquete si tiene conexion a internet
      Cuando pase el carnet por el torniquete
      Entonces se debita de mi saldo en base a mi ruta
      Y se me muestra mi saldo como $0.15
      Y se me muestra el mensaje no dispone de monto suficiente
