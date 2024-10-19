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
Documentación de la biblioteca (API) importada 'random':
https://docs.python.org/3/library/random.html
"""
import random

"""
================== Datos constantes ==========================================

Una persona promedio genera 1.1 kilos de basura.

Fuente: World Bank, What a Waste 2.0 (2018)
https://openknowledge.worldbank.org/handle/10986/30317

La basura total recolectada, un 11% son plásticos, un 14.2% son papel y cartón,
un 1.8% es aluminio.

Fuente: INEGI, Censo Nacional de Gobiernos Municipales y Demarcaciones
Territoriales de la Ciudad de México 2019
https://www.inegi.org.mx/programas/cngmd/2019/
"""

BASURA_GENERADA_POR_PERSONA_AL_DIA = 1.1  # kg de basura generada por persona al día

PORCENTAJE_MATERIALES = {
    "plastico": 0.11,    # 11% de la basura total son plasticos
    "papel": 0.071,      # 14.2% corresponde a papel y cartón
    "carton": 0.071,
    "aluminio": 0.018    # 1.8% corresponde al aluminio
}

"""
================== Cálculos de emisiones ====================================

Emisiones GEI (CO2-eq) Disposición de RSU (toneladas) / Reciclados RSU (toneladas)
De acuerdo a datos de Acapulco obtenidos de Emisiones de Gases de Efecto 
Invernadero en Vertederos de Residuos Sólidos Urbanos (2017), 317,173
toneladas de residuos que generan entre todos los habitantes, generan 412,367 
toneladas de emisiones GEI (CO2-eq).
"""

# Datos de emisiones basados en el estudio de Acapulco
basura_generada_acapulco_ton = 317173
emisiones_gei_acapulco = 412367
emisiones_gei_por_tonelada = emisiones_gei_acapulco / basura_generada_acapulco_ton

# Un promedio normal de un recorrido de un vehiculo en un año está entre 15000 a 27000
kilometros_promedio_anual = 15000
toneladas_gei_por_kilometro = 143 / 1000000

"""
================== Funciones de manejo de usuarios ==========================

Por cuestiones de optimización se generarán datos al azar de usuarios que,
en base a sus puntos, generen estadísticas.

Nota: Los usuarios en BioWay App, cada vez que brindan sus reciclables 
obtienen 20 puntos.
"""

def crear_usuario(id_usuario):
    """Crea un nuevo usuario con id, puntos iniciales en cero y lista vacía."""
    return {
        "id": id_usuario,
        "puntos": 0,
        "recolecciones": []
    }
    
def agregar_recoleccion(usuario, material, cantidad):
    """Agrega una nueva recolección al usuario y aumenta sus puntos."""
    usuario["recolecciones"].append((material, cantidad))
    usuario["puntos"] += 20
    
def calcular_basura_total(usuario):
    """Calcula el total de basura reciclada por usuario."""    
    return sum(cantidad for _, cantidad in usuario["recolecciones"])

"""
================== Funciones de generación de datos aleatorios ==============
"""

def generar_usuarios_aleatorios(num_usuarios):
    """Genera una lista de usuarios con datos aleatorios de reciclaje."""
    usuarios = []
    
    for i in range(num_usuarios):
        usuario = crear_usuario(i + 1)
        num_recolecciones = random.randint(1, 10)
        
        for _ in range(num_recolecciones):
            material = random.choice(list(PORCENTAJE_MATERIALES.keys()))
            cantidad = round(random.uniform(0.5, 5), 2)
            agregar_recoleccion(usuario, material, cantidad)
            
        usuarios.append(usuario)
        
    return usuarios

"""
================== Funciones de cálculo de emisiones ========================
"""

def calcular_emisiones_evitadas(total_reciclado):
    """Calcula las emisiones de GEI evitadas por cantidad reciclada."""
    emisiones_evitadas = (total_reciclado / 1000) * emisiones_gei_por_tonelada
    return emisiones_evitadas

def calcular_equivalencia_carro(emisiones_evitadas):
    """Calcula años equivalentes de no uso de automóvil por emisiones evitadas."""
    emisiones_equivalente_anio = emisiones_evitadas / (
        toneladas_gei_por_kilometro * kilometros_promedio_anual
    )
    return emisiones_equivalente_anio

"""
================== Funciones de presentación de datos =======================
"""

def mostrar_estadisticas(usuario):
    """Muestra estadísticas de reciclaje y emisiones evitadas del usuario."""
    basura_total = calcular_basura_total(usuario)
    print(f"\nEstadísticas del Usuario {usuario['id']}:")
    print(f"Puntos acumulados: {usuario['puntos']}")
    print(f"Número de recolecciones: {len(usuario['recolecciones'])}")
    print(f"Total de basura reciclada: {basura_total:.2f} kg")
    
    materiales_reciclados = {material: 0 for material in PORCENTAJE_MATERIALES}
    for material, cantidad in usuario["recolecciones"]:
        materiales_reciclados[material] += cantidad
    
    for material, cantidad in materiales_reciclados.items():
        print(f"{material.capitalize()} reciclado: {cantidad:.2f} kg")
        
    total_reciclado = sum(materiales_reciclados.values())
    emisiones_evitadas = calcular_emisiones_evitadas(total_reciclado)
    print(
        f"\nEmisiones de CO2 evitadas: {emisiones_evitadas:.2f} toneladas"
    )
    print(
        f"Equivalente a no usar un carro durante "
        f"{calcular_equivalencia_carro(emisiones_evitadas):.2f} años"
    )

"""
================== Función main del programa ===========================
"""

def main():
    """Función principal que maneja la interacción con el usuario."""
    try:
        num_usuarios = int(input("Ingrese el número de usuarios a generar: "))
        if num_usuarios <= 0:
            raise ValueError("El número de usuarios debe ser positivo")
        usuarios = generar_usuarios_aleatorios(num_usuarios)
        
        while True:
            print("\n1. Mostrar estadísticas de todos los usuarios")
            print("2. Mostrar estadísticas de un usuario específico")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                for usuario in usuarios:
                    mostrar_estadisticas(usuario)
            elif opcion == "2":
                id_seleccionado = int(
                    input("Ingrese el identificador del usuario: ")
                )
                usuario = next(
                    (u for u in usuarios if u["id"] == id_seleccionado),
                    None
                )
                
                if usuario:
                    mostrar_estadisticas(usuario)
                else:
                    print("Usuario no válido")
            elif opcion == "3":
                break
            else:
                print("Opción inválida. Seleccione una opción de nuevo.")
                
    except ValueError as e:
        print(f"Error: {e}")
        return
            
if __name__ == "__main__":
    main()