"""
Proyecto Emisiones de Gases de Efecto Invernadero (ton) evitadas con BioWay
Calcula las emisiones GEI evitadas por reciclar en BioWay.
"""

BASURA_GENERADA_POR_PERSONA_AL_DIA = 1.1 # kg de basura generada por persona al día
PORCENTAJE_PLASTICO = 0.11 # 11% de la basura total son plasticos
PORCENTAJE_CARTON_PAPEL = 0.142 # 14.2% corresponde a papel y cartón
PORCENTAJE_ALUMINIO = 0.018 # 1.8% corresponde al aluminio

"""Emisiones GEI (CO2-eq) Disposición de RSU (toneladas) / Reciclados RSU (toneladas)"
De acuerdo a datos de Acapulco obtenidos de Emisiones de Gases de Efecto Invernadero en Vertederos de Residuos Sólidos Urbanos (2017), 317,173
toneladas de residuos que generan entre todos los habitantes, generan 412,367 toneladas de emisiones GEI (CO2-eq)..
"""
basuraGeneradaEnAcapulcoTON = 317173

emisionesGEIGeneradasEnAcapulco = 412367

emisionesGEIPorToneladaDeBausra = emisionesGEIGeneradasEnAcapulco/basuraGeneradaEnAcapulcoTON


"""Los usuarios en BioWay App, cada vez que birndan sus reciclables obtienen 20 puntos"""

#Se añade una función que establece una meta de emisiones evitadas, dicha meta establecida por el usuario

def materialReciclado(basura,porcentajeMaterial):
            return basura * porcentajeMaterial

def metaAlcanzarEmisiones():
    
    materiales_brindados = []
    
    while True:
            metaEmisiones = float(input("Ingresa la meta de toneladas de emisiones GEI que deseas evitar: "))
            if metaEmisiones <=0:
                print("La meta debe ser de un número positivo.")
                continue
            break
    
    puntosUsuario = int(input("Ingresa el número de puntos que tienes en tu BioWay App: "))

    #numVecesUsuarioBrinda = puntosUsuario/20 #Cada vez que el usuario brinda sus reciclables obtiene 20 puntos
    numVecesUsuarioBrinda = 0
    
    while puntosUsuario >= 20:
        puntosUsuario -= 20
        numVecesUsuarioBrinda += 1
        materialRecicladoUsuario = input(f"Ingresa el material que brindaste en la ocacsión {numVecesUsuarioBrinda}, (plástico, papel, cartón, aluminio): ").lower()
        materiales_brindados.append(materialRecicladoUsuario)

    basuraTotalUsuario = BASURA_GENERADA_POR_PERSONA_AL_DIA * numVecesUsuarioBrinda #Determinar la basura reciclable brindada
    #__________________________________________________________________________________________________________________________

    "¿Cuánto representa cada material (cartón, papel, aluminio) respecto a la basura total para determinar la basura brindada?"

    #PUEDE CONVERTIRSE EN UNA FUCNION FUNCION (basuraTotalUsuario, Porcentaje_Plastico)

        
    
    plasticoReciclado = materialReciclado(basuraTotalUsuario,PORCENTAJE_PLASTICO) #en kg

    cartonPapelReciclado = materialReciclado(basuraTotalUsuario,PORCENTAJE_CARTON_PAPEL) #en kg

    aluminioReciclado = materialReciclado(basuraTotalUsuario,PORCENTAJE_ALUMINIO) #en kg

    #__________________________________________________________________________________________________________________________

    "Calculo de emisiones CO2-eq evitadas"
    totalReciclado = plasticoReciclado + cartonPapelReciclado + aluminioReciclado

    "                    Convertir kg a toneladas"
    emisionesEvitadas = (totalReciclado / 1000) * emisionesGEIPorToneladaDeBausra

    #_________________________________________________________________________________________________________________________
    toenladas_GEI_por_kilometro_carro = 143 / 1000000
    toneladas_GEI_año_carro = toenladas_GEI_por_kilometro_carro * 15000 #15,000 km

    #_________________________________________________________________________________________________________________________


    #El ":.2f" es para reducirlo a 2 decimales los resultados

    print(f"\nFelicidades! Has brindado un total de {numVecesUsuarioBrinda} veces tus reciclables, aproximadamente {basuraTotalUsuario:.2f} kg de residuos.")
    print(f"\nDe los cuales {plasticoReciclado:.2f} kg son plastico, y {cartonPapelReciclado:.2f} kg son de Cartón y/o Papel.")
    print(f"\n¡Has evitado aproximadamente {emisionesEvitadas:.2f} toneladas de CO2 por reciclar!")
    
    #_________________________________________________________________________________________________________________________
    
    #Verificar si alcanzó la meta
    if emisionesEvitadas > metaEmisiones:
        print(f"¡Felicidades! Has alcanzado tu meta de evitar {metaEmisiones:.2f} toneladas de CO2.")
    else:
        #Calcular cuántas veces más debe brindar para alcanzar la meta por regla de tres
        vecesFaltantes = (metaEmisiones * numVecesUsuarioBrinda)/emisionesEvitadas
        print(f"\nTe faltan aproximadamente {vecesFaltantes:.2f} veces más de brindar basura para alcanzar tu meta.")



    #Equivalencia de toneladas de CO2 evitadas PUEDE SER UNA FUNCION TAMBIEN funcion(emisionesEvitadas)

    """Un promedio normal que se puede esperar del recorrido de un vehiculo en un año oscila entre 15000 a 27000"""
    if emisionesEvitadas >= toneladas_GEI_año_carro:
        print(f"Has evitado el equivalente al uso del carro durante un año")

    print("\nMateriales que ha brindado: ")
    for i, materialRecicladoUsuario in enumerate(materiales_brindados, 1):
        print(f"{i}. {materialRecicladoUsuario}")

    print("\nRecuerda que con BioWay Juntos por un Mundo Mejor")

    "Esto equivaldría a....." #HACER    

metaAlcanzarEmisiones()