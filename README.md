# Bienvenido al Monitoreo de tus acciones de BioWay!

**Contexto:**

BioWay, la innovadora plataforma de reciclaje que conecta a quienes desean reciclar sus residuos con recolectores informales, ha transformado la manera en que los usuarios contribuyen al cuidado del medio ambiente. Además de facilitar el proceso de reciclaje, BioWay ahora ofrece una herramienta que permite a los usuarios calcular cuántas emisiones de CO2 han ayudado a reducir, basado en el número de recolecciones que han realizado.


# Funcionalidad

Este programa simula usuarios de BioWay con datos aleatorios de reciclaje y calcula las emisiones de gases de efecto invernadero (GEI) evitadas a través de sus esfuerzos de reciclaje. Las principales características incluyen:

  * Generación de datos aleatorios de usuarios con actividades de reciclaje.
  * Cálculo del total de residuos reciclables brindados por usuario.
  * Estimación de emisiones GEI evitadas basadas en materiales reciclados.
  * Conversión de emisiones evitadas a años equivalentes de evitar el uso de un carro.
  * Visualizaión de estadísticas para usuarios individuales o todos los usuarios.

# Instrucciones
Instrucciones:
* Para utilizar esta herramienta de cálculo de emisiones reducidas:
* Abre la app BioWay y dirígete a la sección de tu perfil.
* Toma nota del número de puntos que has acumulado en función de tus recolecciones.
* Ejecuta el código en Python (ver instrucciones abajo) y cuando se te solicite, ingresa tu número de puntos.
* El programa te mostrará cuántas toneladas de CO2 has ayudado a reducir con tus esfuerzos de reciclaje.


## Pseudocódigo

INICIO

1. DEFINIR constantes (basura por persona, porcentajes de materiales, etc.)

2. ENTRADA: número de usuarios a simular (entero)

3. GENERAR usuarios aleatorios
   PARA cada usuario:
     3.1. Asignar ID (entero)
     3.2. Generar recolecciones aleatorias
         PARA cada recolección:
           3.2.1. Elegir material al azar (cadena)
           3.2.2. Asignar cantidad al azar (flotante)

4. MIENTRAS el usuario no elija salir:
   4.1. MOSTRAR menú de opciones
   4.2. ENTRADA: opción del usuario (entero)
   
   4.3. SI opción es mostrar estadísticas de todos los usuarios:
         PARA cada usuario:
           Calcular y mostrar estadísticas
   
   4.4. SI NO, SI opción es mostrar estadísticas de un usuario específico:
         ENTRADA: ID del usuario (entero)
         Buscar usuario
         SI se encuentra:
           Calcular y mostrar estadísticas
         SI NO:
           Mostrar mensaje de error
   
   4.5. SI NO, SI opción es salir:
         Terminar programa
   
   4.6. SI NO:
         Mostrar mensaje de opción inválida

FIN
