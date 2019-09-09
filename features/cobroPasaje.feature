# language: es

Característica: Cobrar pasaje

 @jornadasDeIngreso
  Escenario: Estudiante pagagando pasaje exitoso
      Dado soy estudiante de ESPOL con carnet en la ruta "NORTE"
      Dado que dispongo de 50 en mi carnet estudiantil y el torniquete dispone de conexión a internet
      Cuando acerque mi carnet de ESPOL al torniquete
      Entonces genera el siguiete resultado 'resultado_variable'
      Y tambien ocurre lo siguiente (si es necesario)


