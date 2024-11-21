'''
Las rutas de los CSV se pasarán como argumentos desde main.py.
'''

import pandas as pd

# Función para cargar los datos
def cargar_datos(ruta_empresas, ruta_estudiantes):
    empresas = pd.read_csv(ruta_empresas)
    estudiantes = pd.read_csv(ruta_estudiantes)
    return empresas, estudiantes
