"""
Proyecto Emisiones de Gases de Efecto Invernadero (ton) evitadas con BioWay
Calcula las emisiones GEI evitadas por reciclar en BioWay.
"""

basuraGeneradaPorPersonaPorDia = 1.1 # kg de basura generada por persona al día
porcentajePlastico = 0.11 # 11% de la basura total son plasticos
porcentajeCartonPapel = 0.142 # 14.2% corresponde a papel y cartón

"""Emisiones GEI (CO2-eq) Disposición de RSU (toneladas) / Reciclados RSU (toneladas)"
De acuerdo a datos de Acapulco obtenidos de Emisiones de Gases de Efecto Invernadero en Vertederos de Residuos Sólidos Urbanos (2017), 317,173
toneladas de residuos que generan entre todos los habitantes, generan 412,367 toneladas de emisiones GEI (CO2-eq)..
"""
basuraGeneradaEnAcapulcoTON = 317173

emisionesGEIGeneradasEnAcapulco = 412367

emisionesGEIPorToneladaDeBausra = emisionesGEIGeneradasEnAcapulco/basuraGeneradaEnAcapulcoTON


"""Los usuarios en BioWay App, cada vez que birndan sus reciclables obtienen 20 puntos"""

puntosUsuario = int(input("Ingresa el número de puntos que tienes en tu BioWay App: "))

numVecesUsuarioBrinda = puntosUsuario/20 #Cada vez que el usuario brinda sus reciclables obtiene 20 puntos

basuraTotalUsuario = basuraGeneradaPorPersonaPorDia * numVecesUsuarioBrinda #Determinar la basura reciclable brindada

"Cuánto representa cada material (cartón, papel, aluminio) respecto a la basura total para determinar la basura brindada"
plasticoReciclado = basuraTotalUsuario * porcentajePlastico #en kg

cartonPapelReciclado = basuraTotalUsuario * porcentajeCartonPapel #en kg

"Calculo de emisiones CO2-eq evitadas"
totalReciclado = plasticoReciclado + cartonPapelReciclado

"                    Convertir kg a toneladas"
emisionesEvitadas = (totalReciclado / 1000) * emisionesGEIPorToneladaDeBausra

#El ":.2f" es para reducirlo a 2 decimales los resultados

print(f"Felicidades! Has brindado un total de {numVecesUsuarioBrinda} veces tus reciclables, aproximadamente {basuraTotalUsuario} kg de residuos")
print(f"De los cuales {plasticoReciclado} kg son plastico, y {cartonPapelReciclado:.2f} kg son de Cartón y/o Papel.")
print(f"¡Has evitado aproximadamente {emisionesEvitadas:.2f} toneladas de CO2 por reciclar!")
print("Recuerda que con BioWay Juntos por un Mundo Mejor")

"Esto equivaldría a....." #HACER