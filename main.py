import pandas as pd
import requests
# 1. Simulación de Recolección de Datos de Ventas y Preferencias del Cliente
# Datos simulados de clientes y sus preferencias de compra en productos saludables
clientes_data = {
    'ClienteID': [1, 2, 3, 4, 5],
    'Nombre': ['Ana', 'Luis', 'Carla', 'Pedro', 'Marta'],
    'Preferencia de Productos': ['Orgánico', 'Bajo en Azúcar', 'Sin Gluten', 'Vegetariano', 'Bajo en Sodio'],
    'Frecuencia de Compra': [3, 5, 2, 4, 3]  # compras al mes
}
# Convertir el diccionario en un DataFrame de Pandas
clientes_df = pd.DataFrame(clientes_data)
print("Datos de Clientes y Preferencias de Compra:\n", clientes_df)
# 2. Captura de Respuestas de Encuestas de Satisfacción
# Datos simulados de encuestas de satisfacción con calificación de los clientes (escala 1-5)
encuesta_satisfaccion_data = {
    'ClienteID': [1, 2, 3, 4, 5],
    'Satisfacción con Recomendaciones': [4, 5, 3, 4, 4],
    'Satisfacción con Calidad del Producto': [5, 5, 4, 3, 5],
    'Satisfacción con Sostenibilidad': [4, 4, 3, 5, 5]
}
# Convertir el diccionario en un DataFrame de Pandas
encuesta_df = pd.DataFrame(encuesta_satisfaccion_data)
print("\nDatos de Encuestas de Satisfacción:\n", encuesta_df)
# 3. Integración de Datos Externos (Ej. Estudios sobre Ingredientes y Beneficios de Productos Saludables)
# Supongamos que tenemos un archivo CSV con datos científicos sobre productos saludables.
# Aquí mostramos cómo cargarlo (en este caso, simulamos los datos manualmente)
ingredientes_data = {
    'Producto': ['Proteína Vegetal', 'Té Verde', 'Avena', 'Quinoa', 'Aceite de Coco'],
    'Beneficio': ['Alta en Proteínas', 'Antioxidante', 'Fuente de Fibra', 'Alto en Proteínas', 'Grasa Saludable'],
    'Evidencia Científica': ['Sí', 'Sí', 'Sí', 'Sí', 'Sí']
}
# Convertir el diccionario en un DataFrame de Pandas
ingredientes_df = pd.DataFrame(ingredientes_data)
print("\nDatos de Ingredientes y Beneficios:\n", ingredientes_df)
# Si tienes datos externos en formato CSV, puedes cargarlo con Pandas de esta forma:
# ingredientes_df = pd.read_csv('ruta_al_archivo.csv')
# Ejemplo de integración y análisis inicial de los datos recopilados
# Fusionar los datos de clientes y encuestas de satisfacción según el ClienteID
datos_completos = pd.merge(clientes_df, encuesta_df, on='ClienteID')
print("\nDatos Integrados de Clientes y Satisfacción:\n", datos_completos)
# Fusionar los datos integrados con los datos de ingredientes (en un análisis real, usarías la información de compra)
# Esto es solo ilustrativo
print("\nDatos Finales para Análisis de Clientes y Preferencias de Productos Saludables:\n")
for idx, row in datos_completos.iterrows():
    cliente = row['Nombre']
    preferencia = row['Preferencia de Productos']
    print(f"Cliente: {cliente}, Preferencia: {preferencia}")
    print("Satisfacción en recomendaciones y productos: ", row[['Satisfacción con Recomendaciones',
                                                                'Satisfacción con Calidad del Producto',
                                                                'Satisfacción con Sostenibilidad']].to_dict())
print("\n---\n")

