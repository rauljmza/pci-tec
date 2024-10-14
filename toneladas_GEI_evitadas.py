import random

"""
Proyecto Emisiones de Gases de Efecto Invernadero (ton) evitadas con BioWay
Calcula las emisiones GEI evitadas por reciclar en BioWay.
"""

BASURA_GENERADA_POR_PERSONA_AL_DIA = 1.1 # kg de basura generada por persona al día

"Los porcentajes que representan los materiales del total de basura generada por perosna es constante"

PORCENTAJE_MATERIALES = {
    "plastico": 0.11, # 11% de la basura total son plasticos
    "papel": 0.071, # 14.2% corresponde a papel y cartón
    "carton": 0.071,
    "aluminio": 0.018 # 1.8% corresponde al aluminio
}

"""
Emisiones GEI (CO2-eq) Disposición de RSU (toneladas) / Reciclados RSU (toneladas)
De acuerdo a datos de Acapulco obtenidos de Emisiones de Gases de Efecto Invernadero en Vertederos de Residuos Sólidos Urbanos (2017), 317,173
toneladas de residuos que generan entre todos los habitantes, generan 412,367 toneladas de emisiones GEI (CO2-eq)..
"""
basuraGeneradaEnAcapulcoTON = 317173

emisionesGEIGeneradasEnAcapulco = 412367

emisionesGEIPorToneladaDeBausra = emisionesGEIGeneradasEnAcapulco/basuraGeneradaEnAcapulcoTON

#Un promedio normal que se puede esperar del recorrido de un vehiculo en un año oscila entre 15000 a 27000
   
kilometroPromedioCarroAnual = 15000

toneladasGEIPorKilometroCarro = 143 / 1000000


"""
Por cuestiones de optimización se generarán datos al azar de usuarios que, en base a sus puntos, generen estadísticas

Nota: Los usuarios en BioWay App, cada vez que birndan sus reciclables obtienen 20 puntos
"""
#Se crea el "recipiente" de un usuario, que contiene un id, sus puntos y recolecciones

def crearUsuario(id):
    return {
        "id": id,
        "puntos": 0,
        "recolecciones": []
    }
    
def agregarRecoleccion(usuario, material, cantidad):
    usuario["recolecciones"].append((material,cantidad))
    usuario["puntos"] +=20
    
def calcularBasuraTotal(usuario):
    return sum(cantidad for _, cantidad in usuario["recolecciones"])

#Se añade una función que crea un usuario al azar con el uso de un diccionario para contener su ID que será el número con el que fue creado, así como puntos aleatorios y donaciones realizadas


def generaUsuariosAleatorios(numUsuarios): #Dicha función recibe la cantidad de usuarios que el ejecutor del código define que quiere crear
    
    usuarios = [] #Se define la lista que contendrá a los usuarios, así como sus datos
    
    for i in range(numUsuarios): #Con cada iteración creará un usuario nuevo
        usuario = crearUsuario(i+1)
        
        numRecolecciones = random.randint(1,10)
        
        for _ in range(numRecolecciones):
            
            material = random.choice(list(PORCENTAJE_MATERIALES.keys())) #Elige y crea aleatoriamente para el usuadio como lista un material para asignarle un valor en kilogramos
            
            cantidad = round(random.uniform(0.5, 5 ),2) #Define el rango de aleatoriedad de kilos donados
            
            agregarRecoleccion(usuario,material,cantidad)
            
        usuarios.append(usuario) #Se inserta en la lista del usuario el número de recolecciones, y la cantidad de reciclables donados
        
    return usuarios


def calcularEmisionesEvitadas(totalReciclado): #Se calcularán las emisiones evitadas en base a la función anterior que generó el total en kilogramos reciclado
    return (totalReciclado / 1000) * emisionesGEIPorToneladaDeBausra

def emisionesEquivalenciaCarro(emisionesEvitadas):
    return emisionesEvitadas / (toneladasGEIPorKilometroCarro * kilometroPromedioCarroAnual)

def mostrarEstadisticas(usuario):
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

def main():
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
            idUsuarioSeleccionado = int(input("Ingrese el identificado del usuario (número de usuario): "))
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