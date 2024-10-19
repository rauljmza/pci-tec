"""
Nombre: Raúl Josué Mendoza Medina
Matricula: A01712018

Proyecto Emisiones de Gases de Efecto Invernadero (ton) evitadas con BioWay
Calcula las emisiones GEI evitadas por reciclar en BioWay.
El programa simula usuarios con datos aleatorios de reciclaje y calcula
las emisiones de gases de efecto invernadero evitadas.

"""


"""
================== Librerias ==================================================

Este programa utiliza la biblioteca 'random' de Python para generar datos aleatorios.
Documentación de la biblioteca (API) importada 'random': https://docs.python.org/3/library/random.html
"""
import random


"""
================== Datos constantes ==========================================

Una persona promedio genera 1.1 kilos de basura.

Fuente: World Bank, What a Waste 2.0 (2018)
https://openknowledge.worldbank.org/handle/10986/30317

La basura total recolectada, un 11% son plásticos, un 14.2% son papel y cartón, un 1.8% es aluminio.

Fuente: INEGI, Censo Nacional de Gobiernos Municipales y Demarcaciones
Territoriales de la Ciudad de México 2019
https://www.inegi.org.mx/programas/cngmd/2019/
"""

BASURA_GENERADA_POR_PERSONA_AL_DIA = 1.1 # kg de basura generada por persona al día

PORCENTAJE_MATERIALES = {
    "plastico": 0.11, # 11% de la basura total son plasticos
    "papel": 0.071, # 14.2% corresponde a papel y cartón
    "carton": 0.071,
    "aluminio": 0.018 # 1.8% corresponde al aluminio
}

"""
================== Cálculos de emisiones ====================================

Emisiones GEI (CO2-eq) Disposición de RSU (toneladas) / Reciclados RSU (toneladas)
De acuerdo a datos de Acapulco obtenidos de Emisiones de Gases de Efecto Invernadero en Vertederos de Residuos Sólidos Urbanos (2017), 317,173
toneladas de residuos que generan entre todos los habitantes, generan 412,367 toneladas de emisiones GEI (CO2-eq).

"""

# Datos de emisiones basados en el estudio de Acapulco
basuraGeneradaEnAcapulcoTON = 317173
emisionesGEIGeneradasEnAcapulco = 412367
emisionesGEIPorToneladaDeBausra = emisionesGEIGeneradasEnAcapulco/basuraGeneradaEnAcapulcoTON

# Un promedio normal de un recorrido de un vehiculo en un año está entre 15000 a 27000
kilometroPromedioCarroAnual = 15000
toneladasGEIPorKilometroCarro = 143 / 1000000

"""
================== Funciones de manejo de usuarios ==========================

Por cuestiones de optimización se generarán datos al azar de usuarios que, en base a sus puntos, generen estadísticas.

Nota: Los usuarios en BioWay App, cada vez que birndan sus reciclables obtienen 20 puntos.

"""

def crearUsuario(id):
    """
    ¿Qué hace la función?
    Crea un nuevo usuario con identificador (id), puntos iniciales en cero, y lista de recolecciones vacía.
    
    Recibe: 
        id como valor entero: Identificador del usuario.
        
    Devuelve:
        diccionario ([]): Representa al usuario en cuestión.
    """
    return {
        "id": id,
        "puntos": 0,
        "recolecciones": []
    }
    
def agregarRecoleccion(usuario, material, cantidad):
    """
    ¿Qué hace la función?
    Agrega una nueva recolección al usuario, además aumenta sus puntos.
    
    Recibe:
        usuario como diccionario: Diccionario del usuario (sus datos).
        material como String o cadenta: Matrial reciclado.
        cantidad como flotante que puede recibir decimales: Cantidad de material reciclado.
        
    Devuelve:
        Agrega recolecciones y suma puntos al usuario en su lista en el directorio.
    """ 
    usuario["recolecciones"].append((material,cantidad))
    usuario["puntos"] +=20
    
def calcularBasuraTotal(usuario):
    """
    ¿Qué hace la función?
    Calcula el total de basura reciclada por usuario.
    
    Recibe:
        usuario como diccionario: Diccionario del usuario (sus datos).
        
    Devuelve:
        Total de basura reciclada por el usuario como flotante compatible con decimales.
    """    
    return sum(cantidad for _, cantidad in usuario["recolecciones"])

"""
================== Funciones de generación de datos aleatorios ==============
"""

def generaUsuariosAleatorios(numUsuarios):
    """
    ¿Qué hace la función?    
    Genera una lista de usuarios con datos aleatorios de reciclaje, hace uso de listas, ciclos.
    Nota: Se hace uso de la biblioteca "random" de Python referenciada al inicio del código en la linea 16.
    
    Recibe:
        numUsuarios como valor entero: Números de usuarios a generar.
        
    Devuelve:
        lista ([]): Lista de diccionarios de usuarios.
    """
    usuarios = []
    
    for i in range(numUsuarios):
        usuario = crearUsuario(i+1)
        
        numRecolecciones = random.randint(1,10)
        
        for _ in range(numRecolecciones):
            material = random.choice(list(PORCENTAJE_MATERIALES.keys()))
            cantidad = round(random.uniform(0.5, 5 ),2)
            agregarRecoleccion(usuario,material,cantidad)
            
        usuarios.append(usuario)
        
    return usuarios

"""
================== Funciones de cálculo de emisiones ========================
"""

def calcularEmisionesEvitadas(totalReciclado):
    """
    ¿Qué hace la función?    
    Calcula las emisiones de GEI evitadas basado en la cantidad de material reciclado.
    
    Recibe:
        totalReciclado como flotante compatible con decimales: Total de material reciclado.
        
    Devuelve:
        emisionesEvitadas como flotante compatible con decimales: Emisiones evitadas.
    """
    emisionesEvitadas = (totalReciclado / 1000) * emisionesGEIPorToneladaDeBausra
    
    return emisionesEvitadas

def emisionesEquivalenciaCarro(emisionesEvitadas):
    """
    ¿Qué hace la función?    
    Calcula la equivalencia de emisiones evitadas en años de evitar el uso del carro.
    
    Recibe:
        emisionesEvitadas como flotante compatible con decimales: Emisiones evitadas.
        
    Devuelve:
        emisionesEquivalenteCarro como flotante compatible con decimales: Años evitados de uso de carro.
    """
    emisionesEquivalenteAñoCarro = emisionesEvitadas / (toneladasGEIPorKilometroCarro * kilometroPromedioCarroAnual)
    
    return emisionesEquivalenteAñoCarro

"""
================== Funciones de presentación de datos =======================
"""

def mostrarEstadisticas(usuario):
    """
    ¿Qué hace la función?
    Muestra las estadísticas de reciclaje y emisiones evitadas para un usuario.
    
    Recibe:
        usuario como diccionario: Diccionario del usuario (sus datos).
    
    Devuelve:
        Los datos del usuario y todas sus estadísticas de reciclaje. 
    """
    basuraTotal =  calcularBasuraTotal(usuario)
    print(f"\nEstadísticas del Usuario {usuario['id']}:")
    print(f"Puntos acumulados: {usuario['puntos']}")
    print(f"Número de recolecciones: {len(usuario['recolecciones'])}")
    print(f"Total de basura reciclada: {basuraTotal:.2f} kg")
    
    materialesReciclados = {material: 0 for material in PORCENTAJE_MATERIALES}
    for material, cantidad in usuario["recolecciones"]:
        materialesReciclados[material]+= cantidad
    
    for material, cantidad in materialesReciclados.items():
        print(f"{material.capitalize()} reciclado: {cantidad:.2f} kg")
        
    totalReciclado = sum(materialesReciclados.values())
    emisionesEvitadas = calcularEmisionesEvitadas(totalReciclado)
    print(f"\nEmisiones de CO2 evitadas: {emisionesEvitadas:.2f} toneladas")
    print(f"Equivalente a no usar un carro durante {emisionesEquivalenciaCarro(emisionesEvitadas):.2f} años")

"""
================== Función main del programa ===========================
"""

def main():
    """
    Función main en la que el usuario ejecuta el programa, el usuario puede seleccionar diferentes opciones
    para realizar distintas acciones en el código.
    """
    numUsuarios = int(input("Ingrese el número de usuarios a generar: "))
    usuarios =  generaUsuariosAleatorios(numUsuarios)
    
    while True:
        print("\n1. Mostrar estadísticas de todos los usuarios")
        print("2. Mostrar estadísticas de un usuario específico")
        print("3. Salir")
        opcion = input("Selecciones una opción: ")
        
        if opcion == "1":
            for usuario in usuarios:
                mostrarEstadisticas(usuario)
        elif opcion == "2":
            idUsuarioSeleccionado = int(input("Ingrese el identificador del usuario (número de usuario) para mostrar sus estadísticas específicas: "))
            usuario = next((u for u in usuarios if u["id"]== idUsuarioSeleccionado),None)
            
            if usuario:
                mostrarEstadisticas(usuario)
            else:
                print("Usuario no válido")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Seleccione una opción de nuevo.")
            
if __name__ == "__main__":
    main()