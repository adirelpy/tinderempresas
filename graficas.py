'''
Se llama a esta función desde main.py, pasando coincidencias.

'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap, BoundaryNorm

# Función para graficar el mapa de calor
def graficar_mapa_calor(empresas, estudiantes, coincidencias):
    matriz_coincidencias = np.zeros((len(empresas), len(estudiantes)))

    for coincidencia in coincidencias:
        indice_empresa = empresas[empresas['Nombre'] == coincidencia['Primaria']].index
        indice_estudiante = estudiantes[estudiantes['Nombre'] == coincidencia['Secundaria']].index
        if len(indice_empresa) > 0 and len(indice_estudiante) > 0:
            matriz_coincidencias[indice_empresa[0], indice_estudiante[0]] = coincidencia['Puntuacion']

    colores_personalizados = ListedColormap(['red', 'yellow', 'green'])
    rangos = [0, 33, 66, 100]
    norma = BoundaryNorm(rangos, colores_personalizados.N)

    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz_coincidencias, annot=True, fmt=".0f", cmap=colores_personalizados, norm=norma,
                xticklabels=estudiantes['Nombre'], yticklabels=empresas['Nombre'], cbar=False)
    plt.title('Mapa de Calor: Coincidencias Empresas-Estudiantes (Rojo, Amarillo, Verde)')
    plt.xlabel('Estudiantes')
    plt.ylabel('Empresas')
    plt.show()

# Función para graficar las coincidencias por empresa o estudiante
def graficar_barras(coincidencias, tipo):
    conteo = pd.DataFrame(coincidencias)[tipo].value_counts()

    plt.figure(figsize=(10, 6))
    conteo.plot(kind='bar', color='skyblue' if tipo == 'Primaria' else 'lightgreen')
    plt.title(f'Número de coincidencias por {"Empresa" if tipo == "Primaria" else "Estudiante"}')
    plt.xlabel('Empresas' if tipo == 'Primaria' else 'Estudiantes')
    plt.ylabel('Número de coincidencias')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def graficar_circular(data, titulo):
    """Genera un gráfico circular basado en un DataFrame y una columna."""
    distribucion = data['Sector'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(distribucion, labels=distribucion.index, autopct='%1.1f%%', startangle=90)
    plt.title(titulo)
    plt.show()
