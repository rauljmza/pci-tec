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

emisionesGEIPorToneladaDeBausra = basuraGeneradaEnAcapulcoTON/emisionesGEIGeneradasEnAcapulco



