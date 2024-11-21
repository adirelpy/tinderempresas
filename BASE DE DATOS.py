import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap, BoundaryNorm

# Rutas de los archivos CSV
ruta_empresas = r'C:\Users\usuario\Desktop\PROYECTO TINDER EMPRESAS\empresas.csv'
ruta_estudiantes = r'C:\Users\usuario\Desktop\PROYECTO TINDER EMPRESAS\estudiantes.csv'

# Cargar los datos desde los ficheros CSV
empresas = pd.read_csv(ruta_empresas)
estudiantes = pd.read_csv(ruta_estudiantes)

# Combinar en un solo DataFrame
base_combinada = pd.concat([empresas, estudiantes], ignore_index=True)
print(base_combinada)

# Función para calcular coincidencias entre dos entradas (empresa y estudiante o viceversa)
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

# Generar coincidencias entre todas las combinaciones
def encontrar_coincidencias(base_combinada):
    lista_de_coincidencias = []
    for indice_primario in range(len(base_combinada)):
        entrada_primaria = base_combinada.iloc[indice_primario]
        for indice_secundario in range(indice_primario + 1, len(base_combinada)):
            entrada_secundaria = base_combinada.iloc[indice_secundario]
            # Solo comparar empresa con estudiante
            if entrada_primaria['Tipo'] != entrada_secundaria['Tipo']:
                puntuacion_calculada = calcular_puntuacion_general(entrada_primaria, entrada_secundaria)
                if puntuacion_calculada > 50:  # Umbral mínimo
                    lista_de_coincidencias.append({
                        'Primaria': entrada_primaria['Nombre'],
                        'Secundaria': entrada_secundaria['Nombre'],
                        'Puntuacion': puntuacion_calculada
                    })
    return lista_de_coincidencias

# Calcular coincidencias
coincidencias = encontrar_coincidencias(base_combinada)
for coincidencia in coincidencias:
    print(f"{coincidencia['Primaria']} tiene una coincidencia con {coincidencia['Secundaria']} con una puntuación de {coincidencia['Puntuacion']}")

# Crear matriz de coincidencias entre empresas y estudiantes
matriz_coincidencias = np.zeros((len(empresas), len(estudiantes)))

for coincidencia in coincidencias:
    indice_empresa = empresas[empresas['Nombre'] == coincidencia['Primaria']].index
    indice_estudiante = estudiantes[estudiantes['Nombre'] == coincidencia['Secundaria']].index
    if len(indice_empresa) > 0 and len(indice_estudiante) > 0:
        matriz_coincidencias[indice_empresa[0], indice_estudiante[0]] = coincidencia['Puntuacion']

# Graficar mapa de calor con colores personalizados
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

# Graficar distribución de sectores para empresas
distribucion_sectores_empresas = empresas['Sector'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(distribucion_sectores_empresas, labels=distribucion_sectores_empresas.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Sectores: Empresas')
plt.show()

# Graficar distribución de sectores para estudiantes
distribucion_sectores_estudiantes = estudiantes['Sector'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(distribucion_sectores_estudiantes, labels=distribucion_sectores_estudiantes.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Sectores: Estudiantes')
plt.show()


# Contar coincidencias por empresa
coincidencias_por_empresa = pd.DataFrame(coincidencias)['Primaria'].value_counts()

# Contar coincidencias por estudiante
coincidencias_por_estudiante = pd.DataFrame(coincidencias)['Secundaria'].value_counts()

# Graficar coincidencias por empresa
plt.figure(figsize=(10, 6))
coincidencias_por_empresa.plot(kind='bar', color='skyblue')
plt.title('Número de coincidencias por Empresa')
plt.xlabel('Empresas')
plt.ylabel('Número de coincidencias')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Graficar coincidencias por estudiante
plt.figure(figsize=(10, 6))
coincidencias_por_estudiante.plot(kind='bar', color='lightgreen')
plt.title('Número de coincidencias por Estudiante')
plt.xlabel('Estudiantes')
plt.ylabel('Número de coincidencias')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
