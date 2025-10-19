import csv
import os

# Intrroducimos una funcion auxiliar para validar los numeros enteros: 
def solicitar_entero(mensaje):
    # Pide un número entero no negativo y lo valida.
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("Error: Debe ingresar un número entero no negativo.")

def agregar_pais(archivo, datos):

    # Pedir datos del país, controlando que no estén vacíos
    while True:
        nombre = input("Nombre del país: ").strip()
        poblacion = solicitar_entero("Población: ")
        superficie = solicitar_entero("Superficie: ")
        continente = input("Continente: ").strip()
        
        if nombre.isdigit() and continente.isdigit():
            print("Los campos de país y Continente no pueden ser digitos.")
            continue

        if not all([nombre, poblacion, superficie, continente]):
            print("Todos los campos son obligatorios. Intente nuevamente.")
        else:
            break
    
    # Crear diccionario del país
    nuevo_pais = {
        "nombre": nombre.lower(),
        "poblacion": poblacion.replace(',', '').replace('.', ''),
        "superficie": superficie.replace(',', '').replace('.', ''),
        "continente": continente.lower()
    }

    # Aseguramos que el archivo termine con salto de línea
    with open(archivo, 'rb+') as csvfile:
        csvfile.seek(-1, os.SEEK_END)
        ultimo_caracter = csvfile.read(1)
        if ultimo_caracter != b'\n':
            # agregamos salto de línea final si falta
            csvfile.write(b'\n')  
    
    # Agregar al CSV
    try:
        with open(archivo, 'a', newline='', encoding='utf-8') as csvfile:
            escritor = csv.writer(csvfile)
            escritor.writerow([nombre, poblacion, superficie, continente])
    except Exception as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")
        return datos
    
    # Agregar a la lista de datos y devolverla
    datos.append(nuevo_pais)
    print(f"País '{nombre}' agregado correctamente.")
    return datos
