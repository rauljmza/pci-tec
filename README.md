# Bienvenido al Monitoreo de tus acciones de BioWay!

**Contexto:**

BioWay, la innovadora plataforma de reciclaje que conecta a quienes desean reciclar sus residuos con recolectores informales, ha transformado la manera en que los usuarios contribuyen al cuidado del medio ambiente. Además de facilitar el proceso de reciclaje, BioWay ahora ofrece una herramienta que permite a los usuarios calcular cuántas emisiones de CO2 han ayudado a reducir, basado en el número de recolecciones que han realizado.


# Funcionalidad

Cada vez que un usuario marca residuos como listos para recolección en la app BioWay, se le otorgan puntos en su perfil. Estos puntos reflejan la cantidad de veces que el usuario ha reciclado. Con esta nueva herramienta, puedes ingresar el número de puntos obtenidos en la app y recibir una estimación de la cantidad de CO2 que has ayudado a reducir. Esta funcionalidad no solo te brinda una visión clara de tu impacto ambiental, sino que también sirve como motivación adicional para continuar reciclando.

# Instrucciones
Instrucciones:
* Para utilizar esta herramienta de cálculo de emisiones reducidas:
* Abre la app BioWay y dirígete a la sección de tu perfil.
* Toma nota del número de puntos que has acumulado en función de tus recolecciones.
* Ejecuta el código en Python (ver instrucciones abajo) y cuando se te solicite, ingresa tu número de puntos.
* El programa te mostrará cuántas toneladas de CO2 has ayudado a reducir con tus esfuerzos de reciclaje.


## Pseudocódigo

Definición de la constante reduccionPorPuntos:

* Se establece una constante que representa la cantidad de CO2 que se reduce por cada punto que el usuario ha acumulado en la app. Para este ejemplo, se asume que cada 20 puntos equivalen a 0.5 kg de CO2 reducido.
* Solicitar el número de puntos al usuario:
* El programa pide al usuario que ingrese su número de puntos, que representa las veces que ha reciclado utilizando la app BioWay.

Calcular la reducción de CO2:
* El programa realiza un cálculo simple dividiendo el número de puntos que ingresó el usuario ente 20 por la cantidad de CO2 reducido por cada 20 puntos (reduccion_por_punto). El resultado es la cantidad total de CO2 que el usuario ha ayudado a reducir.
* Mostrar el resultado al usuario:
Se presenta al usuario el resultado del cálculo, que muestra cuántos kilogramos de CO2 ha reducido gracias a sus esfuerzos de reciclaje.
