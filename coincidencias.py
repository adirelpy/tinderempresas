'''
Este módulo depende de empresas y estudiantes, que se cargarán desde cargar_datos.py.
'''



import numpy as np

# Función para calcular puntuaciones entre dos entradas
def calcular_puntuacion_general(entrada_primaria, entrada_secundaria):
    puntuacion_total = 0
    if entrada_primaria['Sector'] == entrada_secundaria['Sector']:
        puntuacion_total += 50
    if entrada_primaria['Ubicacion'] == entrada_secundaria['Ubicacion']:
        puntuacion_total += 30
    detalles_primarios = entrada_primaria['Detalles'].split(', ')
    detalles_secundarios = entrada_secundaria['Detalles'].split(', ')
    if any(detalle in detalles_secundarios for detalle in detalles_primarios):
        puntuacion_total += 20
    return puntuacion_total

# Función para encontrar coincidencias entre empresas y estudiantes
def encontrar_coincidencias(empresas, estudiantes):
    lista_de_coincidencias = []
    for _, empresa in empresas.iterrows():
        for _, estudiante in estudiantes.iterrows():
            puntuacion = calcular_puntuacion_general(empresa, estudiante)
            if puntuacion > 50:  # Umbral mínimo
                lista_de_coincidencias.append({
                    'Primaria': empresa['Nombre'],
                    'Secundaria': estudiante['Nombre'],
                    'Puntuacion': puntuacion
                })
    return lista_de_coincidencias
