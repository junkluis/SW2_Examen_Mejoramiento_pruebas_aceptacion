# language: es

Característica: Cobrar pasaje

 @jornadasDeIngreso
  Escenario: Estudiante pagagando pasaje exitoso
      Dado soy estudiante de ESPOL con carnet en la ruta "NORTE"
      Dado que dispongo de 20 en mi carnet estudiantil y el torniquete dispone de conexión a internet
      Cuando acerque mi carnet de ESPOL al torniquete
      Entonces se me escontará '0.30'

 @jornadasDeIngreso
  Escenario: Estudiante pagagando pasaje con saldo en contra
      Dado soy estudiante POLITECNICO con carnet en la ruta "NORTE"
      Dado que dispongo de 0.10 en mi carnet estudiantil y el torniquete dispone de conexión a internet
      Cuando acerque mi carnet de ESPOL al torniquete
      Entonces me presentará el mensaje: 'Error: No dispone de monto suficiente'




