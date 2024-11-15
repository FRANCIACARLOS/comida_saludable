import pandas as pd
import requests
# 1. Simulación de Recolección de Datos de Ventas y Preferencias del Cliente
# Datos simulados de clientes y sus preferencias de compra en productos saludables
clientes_data = {
    'ClienteID': [1, 2, 3, 4, 5], #Identificador único de cada cliente
    'Nombre': ['Ana', 'Luis', 'Carla', 'Pedro', 'Marta'],# Nombres de los clientes
    'Edad':[25,34,29,45,52],# Edad de cada cliente
    'Peso':[68,75,55,82,70],# Peso de cada cliente en Kilogramos
    'Preferencia de Productos': ['Orgánico', 'Bajo en Azúcar', 'Sin Gluten', 'Vegetariano', 'Bajo en Sodio'], # Preferencia que tiene cada cliente para comprar
    'Frecuencia de Compra': [3, 5, 2, 4, 3], # Número de compras que cada cliente hace al mes
}
# Convertir el diccionario en un DataFrame de Pandas en estructura similar a una hoja de calculo
clientes_df = pd.DataFrame(clientes_data)
print("Datos de Clientes y Preferencias de Compra:\n", clientes_df) #Imprime en pantalla los datos de los clientes
# 2. Captura de Respuestas de Encuestas de Satisfacción
# Datos simulados de encuestas de satisfacción con calificación de los clientes (escala 1-5)
encuesta_satisfaccion_data = {
    'ClienteID': [1, 2, 3, 4, 5], # Identificador de clientes debe coincidir con el ID cliente para unir los datos
    'Satisfacción con Recomendaciones': [4, 5, 3, 4, 4], # Califica la satisfacción en una escala de (1-5)
    'Satisfacción con Calidad del Producto': [5, 5, 4, 3, 5], #Califica la calidad de los productos
    'Satisfacción con Sostenibilidad': [4, 4, 3, 5, 5], #Califica la sostenibilidad de los productos
    'Prevención de Enfermedades':['Diabetis','Hipertensión','Enfermedad Cardiaca','obesidad','presión arterial elevada'],  #Enfermedades relacionadas con la alimentación del cliente
}
# Convertir el diccionario en un DataFrame de Pandas
encuesta_df = pd.DataFrame(encuesta_satisfaccion_data)
print("\nDatos de Encuestas de Satisfacción:\n", encuesta_df) #Imprime los datos de la encuesta de satisfacción
# 3. Integración de Datos Externos (Ingredientes y Beneficios de Productos Saludables)
# Supongamos que tenemos un archivo CSV con datos científicos sobre productos saludables.
# Aquí mostramos cómo cargarlo (en este caso, simulamos los datos manualmente)
ingredientes_data = {
    'Producto': ['Proteína Vegetal', 'Té Verde', 'Avena', 'Quinoa', 'Aceite de Coco'], # Lista de productos saludables
    'Beneficio': ['Alta en Proteínas', 'Antioxidante', 'Fuente de Fibra', 'Alto en Proteínas', 'Grasa Saludable'], #Beneficio de cada producto
    'Evidencia Científica': ['Sí', 'Sí', 'Sí', 'Sí', 'Sí'] # Indica si existe evidencia que me respalde cada producto
}
# Convertir el diccionario en un DataFrame de Pandas
ingredientes_df = pd.DataFrame(ingredientes_data)
print("\nDatos de Ingredientes y Beneficios:\n", ingredientes_df) #Imprime los datos de los productos y sus beneficios
# Si se tienen datos externos en formato CSV, se pueden cargar con Pandas de esta forma:
# ingredientes_df = pd.read_csv('ruta_al_archivo.csv')
# Ejemplo de integración y análisis inicial de los datos recopilados
# Fusionar los datos de clientes y encuestas de satisfacción según el ClienteID
datos_completos = pd.merge(clientes_df, encuesta_df, on='ClienteID') #Une los datos de clientes y encuestas usando ClienteID
print("\nDatos Integrados de Clientes y Satisfacción:\n", datos_completos) # Imprime los datos combinados
# Fusionar los datos integrados con los datos de ingredientes (en un análisis real, usarías la información de compra)
# Esto es solo ilustrativo
print("\nDatos Finales para Análisis de Clientes y Preferencias de Productos Saludables:\n")
for idx, row in datos_completos.iterrows(): # Repite en (datos completos) y devuelve (iterrows) el indice (idx) y la fila (row) en cada ciclo 
    cliente = row['Nombre'] #Extrae los valores de cada fila (nombre)
    edad=row['edad'] #Extrae los valores de cada fila (edad)
    peso=row['peso'] #Extrae los valores de cada fila (peso)
    prevencion = row['Prevencion'] #Extrae los valores de cada fila (prevencion)
    preferencia = row['Preferencia de Productos'] #Extrae los valores de cada fila (preferencia)
    print(f"Cliente: {cliente}, Edad:{edad}, Peso:{peso}Kg, Preferencia: {preferencia},Prevención de Enfermedades:{prevencion}") #mprime la información del cliente, incluyendo nombre, edad, peso, preferencia de productos y enfermedades que intenta prevenir.
    print("Satisfacción en recomendaciones y productos: ", row[['Satisfacción con Recomendaciones',
                                                                'Satisfacción con Calidad del Producto',
                                                                'Satisfacción con Sostenibilidad']].to_dict()) #Convierte los valores de cada cliente y los imprime
print("\n---\n")
# este es un comentario de prueba

